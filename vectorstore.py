from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

DB_DIR = "chroma_db"


def load_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


def load_vectorstore():
    embeddings = load_embeddings()

    db = Chroma(
        persist_directory=DB_DIR,
        embedding_function=embeddings
    )

    print("📦 Vectorstore loaded successfully")
    return db


def get_retriever(k=3):
    db = load_vectorstore()
    return db.as_retriever(search_kwargs={"k": k})