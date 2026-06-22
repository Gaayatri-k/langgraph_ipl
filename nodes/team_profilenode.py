from vectorstore import get_vectorstore

def team_profile_node(state):

    db = get_vectorstore()

    docs = db.similarity_search(
        state["user_query"],
        k=3,
        filter={"section": "team"}
    )
    print("\n=== TEAM PROFILE DOCS ===")

    for i, doc in enumerate(docs):
        print(f"\nDOC {i+1}")
        print(doc.page_content[:500])

    state["team_context"] = docs

    return state