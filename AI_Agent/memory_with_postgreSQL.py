# pip install -U "langgraph-checkpoint-postgres[psycopg]"

from langgraph.checkpoint.postgres import PostgresSaver
from langchain.agents import create_agent

DB_URI = (
    "postgresql://postgres:password@localhost:5432/"
    "receivai?sslmode=disable"
)

with PostgresSaver.from_conn_string(DB_URI) as checkpointer:

    checkpointer.setup()

    agent = create_agent(
        model=model,
        tools=[get_current_time_info],
        checkpointer=checkpointer
    )

    config = {
        "configurable": {
            "thread_id": "customer_101"
        }
    }

    result = agent.invoke(
        {
            "messages": [
                {"role": "user", "content": "Hello"}
            ]
        },
        config=config
    )

    print(result["messages"][-1].content)