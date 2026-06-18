from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

DB_DIR = "chroma_db"

def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

def get_vectorstore():
    return Chroma(
        persist_directory=DB_DIR,
        embedding_function=get_embeddings()
    )