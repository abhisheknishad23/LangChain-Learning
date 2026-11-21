from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver

class State(TypedDict):
    question:str
    answer:str

def answer_node(state: State):
    return{
        "answer":f"Answer:{state['question']}"
    }

builder = StateGraph(State)
builder.add_node("answer", answer_node)
builder.add_edge(START,"answer")
builder.add_edge("answer",END)

checkpointer = InMemorySaver()

graph = builder.compile(
    checkpointer=checkpointer
)

config = {
    "configurable":{
        "thread_id":"user_101"
    }
}

config_1 = {
    "configurable": {
        "thread_id": "user_102"
    }
}

config_2 = {
    "configurable": {
        "thread_id": "user_103"
    }
}

result = graph.invoke(
    {
        "question":"what is RAG",
        "answer":""
    },
    config=config
)

print(result)