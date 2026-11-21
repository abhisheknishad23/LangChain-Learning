from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START,END

class ReviewState(TypedDict, total=False):
    draft:str
    revisions:int
    quality:int

def generate_draft(state: ReviewState):
    revision = state.get("revisions",0)+1
    return{
        "draft":f"Imporoved answer, revision {revision}",
        "revision": revision
    }

def quality_check(state: ReviewState):
    quality = min(
        100,
        60 + state["revisions"]*15
    )

    return{
        "quality": quality
    }

def route_after_review(state: ReviewState):
    if state["quality"] >= 8:
        return "done"
    if state["revisions"] >=3:
        return "done"

    return "revise"

builder = StateGraph(ReviewState)
builder.add_node("draft", generate_draft)
builder.add_node("review",quality_check)
builder.add_edge(START,"draft")
builder.add_edge("draft","review")

builder.add_conditional_edges(
    "review",
    route_after_review,
    {
        "revise":"draft",
        "done": END
    }
)

graph = builder.compile()
result = graph.invoke({
    "draft":"",
    "revisions":0,
    "quality":0
})

print(result)