from vectorstore import get_vectorstore

def records_node(state):

    db = get_vectorstore()

    docs = db.similarity_search(
        state["user_query"],
        k=1
    )

    print("\n=== RETRIEVED DOCS ===")

    for i, doc in enumerate(docs):
        print(f"\nDOC {i+1}")
        print(doc.page_content[:500])

    state["records_context"] = docs

    return state
