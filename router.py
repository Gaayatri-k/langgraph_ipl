def router(state):
    q = state["query"].lower()

    team_map = {
        "mi": "Mumbai Indians",
        "csk": "Chennai Super Kings",
        "rcb": "Royal Challengers Bengaluru",
        "gt": "Gujarat Titans"
    }

    # ENTITY DETECTION FIRST
    for key in team_map:
        if key in q:
            state["entity"] = team_map[key]
            state["query_type"] = "team"
            return state

    # KEYWORD ROUTING
    if "captain" in q or "team" in q:
        state["query_type"] = "team"

    elif "runs" in q or "strike rate" in q:
        state["query_type"] = "batting"

    elif "wickets" in q or "economy" in q:
        state["query_type"] = "bowling"

    elif "vs" in q:
        state["query_type"] = "h2h"

    elif "pitch" in q or "stadium" in q:
        state["query_type"] = "venue"

    else:
        state["query_type"] = "records"

    return state