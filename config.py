import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
CHAT_MODEL = os.getenv("CHAT_MODEL", "nvidia/nemotron-3-ultra-550b-a55b:free")
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
EMBEDDING_DIM = 384
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
FAISS_INDEX_DIR = os.path.join(DATA_DIR, "faiss_index")
