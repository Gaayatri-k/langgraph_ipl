from vectorstore import get_vectorstore

def team_node(state):
    db = get_vectorstore()

    docs = db.similarity_search(
        state["user_query"],
        k=3
    )

    state["team_context"] = docs

    return state