import os
import json
import faiss
import numpy as np
from langchain_core.documents import Document
from core.embeddings import embed_documents, embed_query, get_model
from config import FAISS_INDEX_DIR, EMBEDDING_DIM


def _get_index_path() -> str:
    return os.path.join(FAISS_INDEX_DIR, "index.faiss")


def _get_docstore_path() -> str:
    return os.path.join(FAISS_INDEX_DIR, "docstore.json")


def _ensure_dir():
    os.makedirs(FAISS_INDEX_DIR, exist_ok=True)


def _get_model():
    return get_model()


class VectorStore:
    def __init__(self):
        self.index: faiss.IndexFlatL2 | None = None
        self.documents: list[Document] = []
        self._load()

    def _load(self):
        index_path = _get_index_path()
        docstore_path = _get_docstore_path()

        if os.path.exists(index_path) and os.path.exists(docstore_path):
            self.index = faiss.read_index(index_path)
            with open(docstore_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.documents = [
                    Document(page_content=d["page_content"], metadata=d["metadata"])
                    for d in data
                ]
        else:
            self.index = faiss.IndexFlatL2(EMBEDDING_DIM)

    def _save(self):
        _ensure_dir()
        faiss.write_index(self.index, _get_index_path())
        data = [
            {"page_content": doc.page_content, "metadata": doc.metadata}
            for doc in self.documents
        ]
        with open(_get_docstore_path(), "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)

    def add_documents(self, documents: list[Document]) -> int:
        if not documents:
            return 0

        texts = [doc.page_content for doc in documents]
        embeddings = embed_documents(texts)
        vectors = np.array(embeddings, dtype=np.float32)

        self.index.add(vectors)
        self.documents.extend(documents)
        self._save()
        return len(documents)

    def search(self, query: str, k: int = 5, threshold: float = 0.5) -> list[tuple[Document, float]]:
        if self.index is None or self.index.ntotal == 0:
            return []

        query_vec = np.array([embed_query(query)], dtype=np.float32)
        actual_k = min(k, self.index.ntotal)
        distances, indices = self.index.search(query_vec, actual_k)

        results = []
        for dist, idx in zip(distances[0], indices[0]):
            if idx == -1:
                continue
            similarity = 1 / (1 + dist)
            if similarity >= threshold:
                results.append((self.documents[idx], similarity))

        return results

    @property
    def count(self) -> int:
        return self.index.ntotal if self.index else 0

    def clear(self):
        self.index = faiss.IndexFlatL2(EMBEDDING_DIM)
        self.documents = []
        if os.path.exists(_get_index_path()):
            os.remove(_get_index_path())
        if os.path.exists(_get_docstore_path()):
            os.remove(_get_docstore_path())
