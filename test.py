from vectorstore import get_vectorstore

db = get_vectorstore()

docs = db.similarity_search(
    "Tell me about MI",
    k=3,
    filter={"section": "team"}
)

for doc in docs:
    print(doc.metadata["section"])
    print(doc.page_content[:300])
    print("-" * 50)