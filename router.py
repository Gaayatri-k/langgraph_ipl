def router(state):
    query=state['query'].lower()
    if "captain" in query:
        state["query_type"]="team"
    elif "runs" in query:
        state["query_type"]="batting"
    elif "wickets" in query:
        state["query_type"]="bowling"
    elif "dream11" in query:
        state["query_type"]="dream11"
    else:
        state["query_type"]="unknown"
    return state   