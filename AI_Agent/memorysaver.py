from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI

from langgraph.checkpoint.memory import InMemorySaver


@tool
def get_current_time_info() -> str:
    """Return a simple demonstration message."""
    return "The application is running."


model = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)

checkpointer = InMemorySaver()

agent = create_agent(
    model=model,
    tools=[get_current_time_info],
    checkpointer=checkpointer,
    system_prompt="You are a helpful assistant."
)


# Same thread ID = same conversation
config = {
    "configurable": {
        "thread_id": "user_101"
    }
}


# First message
result1 = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "My name is Abhishek."
            }
        ]
    },
    config=config
)

print(result1["messages"][-1].content)


# Second message
result2 = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "What is my name?"
            }
        ]
    },
    config=config
)

print(result2["messages"][-1].content)