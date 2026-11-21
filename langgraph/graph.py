from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END

#define state
class AgentState(TypedDict):
    question:str
    answer:str

#define node
def process_question(state: AgentState):
    question = state["question"]
    answer = f"Your question is: {question}"

    return{
        "answer":answer
    }

#build graph
builder = StateGraph(AgentState)
builder.add_node(
    "process_question",
    process_question
)

#connect nodes
builder.add_edge(START, "process_question")
builder.add_edge("process_question", END)

#compile graph
graph = builder.compile()

#execute graph
result = graph.invoke({
    "question":"What is LangGraph"
})

print(result)