from vectorstore import get_vectorstore

def trend_node(state):
    db = get_vectorstore()
    print("\n=== TREND NODE CALLED ===")
    docs = db.similarity_search(
        state["user_query"],
        k=3,
        filter={
            "section": "trend"
        }
    )
    print(f"Retrieved docs: {len(docs)}")

    for i, doc in enumerate(docs):
        print(f"\nDOC {i+1}")
        print("-" * 50)
        print(doc.page_content[:1000])
        print("-" * 50)

    state["trend_context"] = docs

    return state