from vectorstore import get_vectorstore

def bowling_node(state):

    db = get_vectorstore()

    docs = db.similarity_search(
        state["user_query"],
        k=5,
        filter={"section": "bowling"}
    )
    print("\n=== RETRIEVED DOCS ===")

    for i, doc in enumerate(docs):
        print(f"\nDOC {i+1}")
        print(doc.page_content[:300])

    state["bowling_context"] = docs

    return state
