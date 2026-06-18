from typing import TypedDict, List
from langchain_core.documents import Document

class IPLState(TypedDict):

    user_query: str

    query_type: str
    entities: List[str]

    batting_context: List[Document]
    bowling_context: List[Document]
    h2h_context: List[Document]
    venue_context: List[Document]
    form_context: List[Document]
    records_context: List[Document]   # <- add this

    final_answer: str