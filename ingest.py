from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from vectorstore import get_embeddings

loader = PyPDFLoader(
    "data/IPL_LangGraph_RAG_Dataset.pdf"
)

docs = loader.load()

print("Pages:", len(docs))
print("\nFIRST PAGE:\n")
print(docs[0].page_content[:1000])

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)

chunks = splitter.split_documents(docs)

processed_chunks = []

for chunk in chunks:

    text = chunk.page_content.lower()

    section = "unknown"

    if "team profile" in text:
        section = "team"

    elif "batting" in text:
        section = "batting"

    elif "bowling" in text:
        section = "bowling"

    elif "head-to-head" in text or "h2h" in text:
        section = "h2h"

    elif "venue" in text:
        section = "venue"

    elif "record" in text or "milestone" in text:
        section = "records"

    elif "form" in text:
        section = "form"

    elif "trend" in text:
        section = "trend"

    chunk.metadata["section"] = section

    processed_chunks.append(chunk)

print("\n=== SAMPLE METADATA ===")

for i in range(min(5, len(processed_chunks))):
    print(
        f"Chunk {i+1} -> {processed_chunks[i].metadata}"
    )

Chroma.from_documents(
    documents=processed_chunks,
    embedding=get_embeddings(),
    persist_directory="chroma_db"
)

print("\nVector Database Created Successfully!")