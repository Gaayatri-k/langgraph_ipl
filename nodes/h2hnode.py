from vectorstore import get_vectorstore

def h2h_node(state):

    db = get_vectorstore()

    docs = db.similarity_search(
        state["user_query"],
        k=1
    )

    print("\n=== RETRIEVED DOCS ===")

    for i, doc in enumerate(docs):
        print(f"\nDOC {i+1}")
        print(doc.page_content[:300])

    state["h2h_context"] = docs

    return state
