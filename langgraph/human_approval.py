from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import interrupt, Command

class PaymentState(TypedDict, total=False):
    invoice_id:str
    amount: float
    approved:bool
    reviewer:str
    status:str

def prepare_payment(state:PaymentState):
    return{
        "status":"awaiting_approval"
    }

def human_approval(state: PaymentState):
    decision = interrupt({
        "message":"Please approve this payment",
        "invoice_id":state["invoice_id"],
        "amount":state["amount"]
    })

    return{
        "approved": decision["approved"],
        "reviewer": decision["reviewer"]
    }

def route_decision(state: PaymentState):
    if state["approved"]:
        return "approved"
    return "rejected"

def approved_node(state: PaymentState):
    return{
        "status":"approved_for_manual_processing"
    }

def rejected_node(state:PaymentState):
    return{
        "status":"rejected"
    }

builder = StateGraph(PaymentState)

builder.add_node("prepare",prepare_payment)
builder.add_node("approval",human_approval)
builder.add_node("approved", approved_node)
builder.add_node("rejected", rejected_node)
builder.add_edge(START, "prepare")
builder.add_edge("prepare","approval")

builder.add_edge("prepare","approval")

builder.add_conditional_edges(
    "approval",
    route_decision,
    {
        "approved":"approved",
        "rejected":"rejected"
    }
)

builder.add_edge("approved",END)
builder.add_edge("rejected",END)

checkpointer = InMemorySaver()

graph = builder.compile(
    checkpointer=checkpointer
)

#start workflow

config ={
    "configurable":{
        "thread_id":"payment_101"
    }
}

result = graph.invoke(
    {
        "invoice_id":"INV-1001",
        "amount":50000
    },
    config=config
)

print(result.get("__interrupt__"))

#resume after human approval
result = graph.invoke(
    Command(
        resume={
            "approved":True,
            "reviewer":"finance_manager"
        }
    ),
    config=config
)

print(result["status"])