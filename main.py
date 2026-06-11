from router import router
from graph import *

state = {
    "query":"Who captains CSK?"
}
state = router(state)
print(state)

if state["query_type"] == "team":
    team_node(state)

elif state["query_type"] == "batting":
    batting_node(state)

elif state["query_type"] == "bowling":
    bowling_node(state)

elif state["query_type"] == "dream11":
    dream11_node(state)        