from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from vectorstore import get_embeddings

loader = PyPDFLoader(
    "data/IPL_LangGraph_RAG_Dataset.pdf"
)

docs = loader.load()

print("Pages:", len(docs))

for doc in docs:
    print("\n" + "=" * 80)
    print(f"PAGE {doc.metadata['page']}")
    print("=" * 80)
    print(doc.page_content[:300])

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)

chunks = splitter.split_documents(docs)

processed_chunks = []

for chunk in chunks:

    page = chunk.metadata["page"]

    section = "unknown"

    if page == 1:
        section = "team"

    elif page == 2:
        section = "batting"

    elif page == 3:
        section = "bowling"

    elif page == 4:
        section = "h2h"

    elif page in [5, 6]:
        section = "venue"

    elif page == 7:
        section = "trend"

    elif page == 8:
        section = "form"

    elif page == 9:
        section = "records"

    else:
        section = "ignore"

    chunk.metadata["section"] = section

    processed_chunks.append(chunk)
    
print("\n=== PAGE -> SECTION ===")

for chunk in processed_chunks[:20]:
    print(
        f"Page={chunk.metadata['page']} | "
        f"Section={chunk.metadata['section']}"
    )

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