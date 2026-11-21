from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    question:str
    category:str
    response:str

#node 1

def classify(state: State):
    question=state["question"].lower()
    if "invoce" in question:
        category = "invoice"
    else:
        category = "general"
    return{
        "category": category
    }

#node 2
def invoice_node(state: State):
    return{
        "response":"Invoice-related request detected."
    }

#node 3
def general_node(state:State):
    return{
        "response":"General question detected."
    }

#router
def route_question(state: State):
    if state["category"] == "invoice":
        return "invoice"
    return "general"

#build graph
builder = StateGraph(State)
builder.add_node("classify",classify)
builder.add_node("invoice",invoice_node)
builder.add_node("general", general_node)

builder.add_edge(START, "classify")

builder.add_conditional_edges(
    "classify",
    route_question,
    {
        "invoice":"invoice",
        "general":"general"
    }
)

builder.add_edge("invoice",END)
builder.add_edge("general",END)

graph = builder.compile()

#test
result = graph.invoke({
    "question":"Show me my overdue invoice",
    "category":"",
    "response":""
})

print(result)