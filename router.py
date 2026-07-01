def router(state):

    query = state["user_query"].lower()

    teams = [
        "mi","mumbai",
        "csk","chennai",
        "rcb","bangalore",
        "srh","hyderabad",
        "kkr","kolkata",
        "rr","rajasthan",
        "dc","delhi",
        "pbks","punjab",
        "lsg","lucknow",
        "gt","gujarat"
    ]

    # Trend Queries
    if any(word in query for word in [
        "trend",
        "2019",
        "2020",
        "2021",
        "2022",
        "2023",
        "2024",
        "consistent",
        "improved",
        "performance over years"
    ]):
        return "trend"

    # Team profile queries
    if any(team in query for team in teams):
        return "team"

    # Form queries
    if any(word in query for word in [
        "form",
        "last 5",
        "recent",
        "recent matches"
    ]):
        return "form"
    # Bowling queries
    if any(word in query for word in [
        "wicket",
        "wickets",
        "economy",
        "bowling",
        "bumrah",
        "rashid",
        "shami",
        "rabada",
        "chahal",
        "compare"
    ]):
        return "bowling"

    # Batting queries
    if any(word in query for word in [
        "runs",
        "strike rate",
        "century",
        "fifty",
        "kohli",
        "rohit",
        "rahul",
        "gaikwad"
    ]):
        return "batting"
    

    # H2H queries
    if "vs" in query:
        return "h2h"

    # Venue queries
    if any(word in query for word in [
        "venue",
        "stadium",
        "pitch"
    ]):
        return "venue"

    #record queries
    if any(word in query for word in [
        "record",
        "highest",
        "most",
        "fastest",
        "best bowling",
        "milestone"
    ]):
        return "records"