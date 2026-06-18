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
1. Answer ONLY from the provided context.
2. Never use your own cricket knowledge.
3. Return exact numbers from the context.
4. If the answer is not present in the context, say:
   'I could not find the answer in the IPL dataset.'
5. Keep answers concise and factual.
                """
            ),
            (
                "human",
                f"""
Context:
{context}

Question:
{state['user_query']}
"""
            )
        ]
    )

    state["final_answer"] = response.content

    return state