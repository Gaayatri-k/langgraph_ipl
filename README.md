# IPL Multi-Agent RAG System using LangGraph

An intelligent IPL Question Answering System built using LangGraph, LangChain, ChromaDB, HuggingFace Embeddings, and Groq LLM.

The system uses metadata-filtered retrieval and specialized nodes to answer IPL-related questions accurately.

---

## Features

### Team Profile Node
Provides:
- Captain
- Coach
- Home Stadium
- Titles
- Team Information

### Batting Statistics Node
Provides:
- Runs
- Average
- Strike Rate
- Centuries
- Fifties
- Highest Score

### Bowling Statistics Node
Provides:
- Wickets
- Economy
- Bowling Average
- Strike Rate
- Best Figures

### Head-to-Head Node
Provides:
- Matchup records
- Team-vs-Team analysis

### Venue Node
Provides:
- Venue details
- Pitch reports
- Stadium characteristics

### Trend Node
Provides:
- Team performance from 2019–2024
- Consistency analysis
- Historical trends

### Form Node
Provides:
- Last 5 match performance
- Recent player form
- Metadata-filtered retrieval

### Records Node
Provides:
- Highest Team Score
- Highest Individual Score
- Most Runs
- Most Wickets
- Fastest Fifty
- Most Titles
- Highest Partnership
- Highest Chase

---

## Metadata Filtering

The system uses metadata-based retrieval to improve accuracy.

Example:

```python
docs = db.similarity_search(
    query,
    k=3,
    filter={"section": "form"}
)
```

This ensures that form-related questions retrieve only form-related documents.

---

## LangGraph Workflow

```text
User Query
    |
 Router
    |
    +--> Team Node
    +--> Batting Node
    +--> Bowling Node
    +--> H2H Node
    +--> Venue Node
    +--> Trend Node
    +--> Form Node
    +--> Records Node
    |
Synthesis Node
    |
Final Answer
```

---

## Tech Stack

- Python
- LangGraph
- LangChain
- ChromaDB
- HuggingFace Embeddings
- Groq LLM

---

## Sample Queries

```text
Who is the captain of RCB?

How many runs has Virat Kohli scored?

Compare Kohli and Rohit Sharma.

How has RCB performed from 2019 to 2024?

Who is in better form, Kohli or Travis Head?

Highest IPL team score?

MI vs CSK head-to-head record?
```

---

## Project Status

### Completed ✅

- Router Node
- Team Profile Node
- Batting Node
- Bowling Node
- H2H Node
- Venue Node
- Trend Node
- Form Node
- Records Node
- Metadata Filtering
- Synthesis Node

### In Progress 🚀

- Dream11 Multi-Agent Workflow
- Validation Node
- Advanced Multi-Node Query Planning

---

## Future Enhancements

- Dream11 Team Recommendation Agent
- Multi-Agent Collaboration
- Query Validation Layer
- Streaming Responses
- Agent Memory

---
