def router(state):

    query = state["user_query"].lower()

    teams = [
        "mi",
        "mumbai",
        "csk",
        "chennai",
        "rcb",
        "bangalore",
        "srh",
        "hyderabad",
        "kkr",
        "kolkata",
        "rr",
        "rajasthan",
        "dc",
        "delhi",
        "pbks",
        "punjab",
        "lsg",
        "lucknow",
        "gt",
        "gujarat"
    ]

    if any(team in query for team in teams):
        return "team"

    if any(word in query for word in ["runs", "strike rate", "century"]):
        return "batting"

    if any(word in query for word in ["wickets", "economy"]):
        return "bowling"

    if "vs" in query:
        return "h2h"

    if any(word in query for word in ["venue", "stadium", "pitch"]):
        return "venue"

    return "records"