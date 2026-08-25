import os

def _get_secret(key: str, default: str = "") -> str:
    try:
        import streamlit as st
        if hasattr(st, "secrets") and key in st.secrets:
            return st.secrets[key]
    except Exception:
        pass
    return os.getenv(key, default)


OPENROUTER_API_KEY = _get_secret("OPENROUTER_API_KEY")
CHAT_MODEL = _get_secret("CHAT_MODEL", "nvidia/nemotron-3-ultra-550b-a55b:free")
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
EMBEDDING_DIM = 384
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
FAISS_INDEX_DIR = os.path.join(DATA_DIR, "faiss_index")
