from vectorstore import get_vectorstore

def batting_node(state):

    db = get_vectorstore()

    docs = db.similarity_search(
        state["user_query"],
        k=3,
        filter={"section": "batting"}
    )
    print("\n=== RETRIEVED DOCS ===")

    for i, doc in enumerate(docs):
        print(f"\nDOC {i+1}")
        print(doc.page_content[:300])

    state["batting_context"] = docs

    return state
