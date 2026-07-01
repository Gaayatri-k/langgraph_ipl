from langgraph.graph import StateGraph, END


from state import IPLState
from router import router

from nodes.team_profilenode import team_profile_node
from nodes.battingnode import batting_node
from nodes.bowlingnode import bowling_node
from nodes.h2hnode import h2h_node
from nodes.venuenode import venue_node
from nodes.recordsnode import records_node
from nodes.synthesisnode import synthesis_node
from nodes.formnode import form_node

graph = StateGraph(IPLState)

graph.add_node("team", team_profile_node)
graph.add_node("batting", batting_node)
graph.add_node("bowling", bowling_node)
graph.add_node("h2h", h2h_node)
graph.add_node("venue", venue_node)
graph.add_node("records", records_node)
graph.add_node("synthesis", synthesis_node)
graph.add_node("form",form_node)

graph.set_conditional_entry_point(
    router,
    {
        "team": "team",
        "batting": "batting",
        "bowling": "bowling",
        "h2h": "h2h",
        "venue": "venue",
        "records": "records",
        "form": "form"
    }
)

graph.add_edge("team", "synthesis")
graph.add_edge("batting", "synthesis")
graph.add_edge("bowling", "synthesis")
graph.add_edge("h2h", "synthesis")
graph.add_edge("venue", "synthesis")
graph.add_edge("records", "synthesis")
graph.add_edge("form","synthesis")

graph.add_edge("synthesis", END)

app = graph.compile()