from dotenv import load_dotenv
load_dotenv()

import os
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

def synthesis_node(state):

    context = ""

    for key in [
        "team_context",
        "batting_context",
        "bowling_context",
        "h2h_context",
        "venue_context",
        "form_context",
        "records_context"
    ]:

        docs = state.get(key, [])

        for doc in docs:
            context += doc.page_content + "\n"

    print("\n=== CONTEXT SENT TO LLM ===")
    print(context[:2000])

    response = llm.invoke(
    [
        (
    "system",
    """
You are an IPL statistics assistant.

Rules:
1. Use ONLY the provided context.
2. Never use outside knowledge.
3. For comparison questions:
   - Compare players metric-by-metric.
   - Use bullet points.
   - Do not add opinions unless directly supported by data.
4. For fact questions:
   - Return exact values only.
5. If answer is not present:
   - Return exactly:
     'I could not find the answer in the IPL dataset.'
"""
),
        (
            "human",
            f"""
Context:
{context}

Question:
{state['user_query']}

Answer:
"""
        )
    ]
)

    state["final_answer"] = response.content

    return state