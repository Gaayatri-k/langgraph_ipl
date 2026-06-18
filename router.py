def router(state):

    query = state["user_query"].lower()

    if "runs" in query:
        return "batting"

    if "wickets" in query:
        return "bowling"

    if "pitch" in query:
        return "venue"

    if "vs" in query:
        return "h2h"

    return "records"