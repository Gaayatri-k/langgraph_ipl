from llm import llm

def synthesis_node(state):
    context = f"""

    {state.get('team_context','')}
    {state.get('batting_context','')}
    {state.get('bowling_context','')}
    {state.get('h2h_context','')}
    {state.get('venue_context','')}
    {state.get('records_context','')}
    """

    prompt = f"""
    Answer using only the context.
    Context:
    {context}
    Question:
    {state['query']}
    """
    response = llm.invoke(prompt)
    state["answer"] = response.content

    return state