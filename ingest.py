from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from vectorstore import get_embeddings

loader = PyPDFLoader(
    "data/IPL_LangGraph_RAG_Dataset.pdf"
)

docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)

chunks = splitter.split_documents(docs)

Chroma.from_documents(
    documents=chunks,
    embedding=get_embeddings(),
    persist_directory="chroma_db"
)
docs = loader.load()

print("Pages:", len(docs))
print("\nFIRST PAGE:\n")
print(docs[0].page_content[:1000])