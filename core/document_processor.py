from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from config import CHUNK_SIZE, CHUNK_OVERLAP
import os
import tempfile


def _get_splitter() -> RecursiveCharacterTextSplitter:
    return RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ". ", " ", ""],
        length_function=len,
    )


def load_pdf(file_path: str) -> list[Document]:
    loader = PyPDFLoader(file_path)
    return loader.load()


def load_text(file_path: str) -> list[Document]:
    loader = TextLoader(file_path, encoding="utf-8")
    return loader.load()


def process_file(uploaded_file, file_name: str) -> list[Document]:
    suffix = os.path.splitext(file_name)[1].lower()

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    try:
        if suffix == ".pdf":
            docs = load_pdf(tmp_path)
        else:
            docs = load_text(tmp_path)

        for doc in docs:
            doc.metadata["source"] = file_name

        splitter = _get_splitter()
        chunks = splitter.split_documents(docs)

        for chunk in chunks:
            chunk.page_content = chunk.page_content.strip()
            chunk.page_content = " ".join(chunk.page_content.split())

        return [c for c in chunks if len(c.page_content) > 10]
    finally:
        os.unlink(tmp_path)


def process_text(text: str, source: str = "pasted_text") -> list[Document]:
    doc = Document(page_content=text, metadata={"source": source})
    splitter = _get_splitter()
    chunks = splitter.split_documents([doc])

    for chunk in chunks:
        chunk.page_content = chunk.page_content.strip()
        chunk.page_content = " ".join(chunk.page_content.split())

    return [c for c in chunks if len(c.page_content) > 10]
