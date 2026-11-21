from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

from langgraph.graph import StateGraph, START, END

from typing_extensions import TypedDict


model = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)


class ResearchState(TypedDict):

    topic: str
    research: str
    analysis: str


# Specialist agent 1
research_agent = create_agent(
    model=model,
    tools=[],
    system_prompt=(
        "You are a research specialist. "
        "Provide factual and structured research."
    )
)


# Specialist agent 2
analyst_agent = create_agent(
    model=model,
    tools=[],
    system_prompt=(
        "You are an analyst. "
        "Analyze the supplied research and identify key insights."
    )
)


# Research node
def research_node(state: ResearchState):

    result = research_agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": f"Research this topic: {state['topic']}"
            }
        ]
    })

    return {
        "research": result["messages"][-1].content
    }


# Analysis node
def analysis_node(state: ResearchState):

    result = analyst_agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": f"Analyze this research: {state['research']}"
            }
        ]
    })

    return {
        "analysis": result["messages"][-1].content
    }


builder = StateGraph(ResearchState)

builder.add_node("research", research_node)

builder.add_node("analysis", analysis_node)

builder.add_edge(START, "research")

builder.add_edge("research", "analysis")

builder.add_edge("analysis", END)

graph = builder.compile()


result = graph.invoke({
    "topic": "Applications of AI in finance",
    "research": "",
    "analysis": ""
})

print(result["analysis"])