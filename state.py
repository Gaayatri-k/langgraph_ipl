from typing import TypedDict

class IPLState(TypedDict):
    query: str
    query_type: str
    team_context: str
    batting_context: str
    bowling_context: str
    h2h_context: str
    venue_context: str
    records_context: str
    answer: str