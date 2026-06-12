from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import os


PDF_PATH = "data/IPL_LangGraph_RAG_Dataset.pdf"
DB_DIR = "chroma_db"


def load_documents():
    """Load PDF and return raw documents"""
    loader = PyPDFLoader(PDF_PATH)
    docs = loader.load()

    print(f"📄 Total Pages Loaded: {len(docs)}")
    return docs


def split_documents(docs):
    """Split documents into chunks"""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(docs)

    print(f"✂️ Total Chunks Created: {len(chunks)}")
    return chunks


def get_embeddings():
    """Load embedding model"""
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


def create_vectorstore(chunks, embeddings):
    """Create and persist Chroma DB"""
    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_DIR
    )

    db.persist()
    print("💾 Vector DB created and saved!")
    return db


def ingest():
    """Main ingestion pipeline"""
    print("🚀 Starting ingestion pipeline...")

    docs = load_documents()
    chunks = split_documents(docs)
    embeddings = get_embeddings()
    db = create_vectorstore(chunks, embeddings)

    print("✅ Ingestion completed successfully!")
    return db


if __name__ == "__main__":
    ingest()