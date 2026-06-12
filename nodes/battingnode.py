from vectorstore import db

def batting_node(state):
    retriever = db.as_retriever(
        search_kwargs={
            "k":3
        }
    )
    docs = retriever.invoke(
        state["query"]
    )
    state["batting_context"] = "\n".join(
        [d.page_content for d in docs]
    )
    return state