from langgraph.checkpoint.postgres import PostgreSaver

DB_URI = (
    "postgresql://postgres:password@localhost:5432/"
    "receivai?sslmode=disable"
)

with PostgreSaver.from_com_string(DB_URI) as saver:
    saver.setup()
    graph = builder.compile(
        checkpointer = saver
    )

    result = graph.invoke(
        {
            "question": "What is RAG",
            "answer":""
        },
        config={
            "configurable":{
                "thread_id":"user_101"
            }
        }
    )
    print(result)