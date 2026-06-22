from vectorstore import get_vectorstore

def venue_node(state):

    db = get_vectorstore()

    docs = db.similarity_search(
        state["user_query"],
        k=3,
        filter={"section": "venue"}
    )
    print("\n=== RETRIEVED DOCS ===")

    for i, doc in enumerate(docs):
        print(f"\nDOC {i+1}")
        print(doc.page_content[:300])
    state["venue_context"] = docs

    return state
