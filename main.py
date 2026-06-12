from graph import app

while True:
    query = input("Ask : ")
    result = app.invoke({
        "query":query
    })
    print("\n")
    print(result["answer"])
    print("\n")