from vectorstore import get_vectorstore

db = get_vectorstore()

def form_node(state):

    docs = db.similarity_search(
        state["user_query"],
        k=3,
        filter={
            "section": "form"
        }
    )

    print("\n=== FORM DOCS ===\n")

    for i, doc in enumerate(docs):
        print(f"DOC {i+1}")
        print(doc.page_content[:500])
        print()

    state["form_context"] = docs

    return state