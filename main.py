from graph import app

query = input("Ask IPL Question: ")

result = app.invoke({
    "user_query": query
})

print(result["final_answer"])