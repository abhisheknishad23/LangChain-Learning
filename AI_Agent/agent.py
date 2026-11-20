from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents import create_agent

load_dotenv()

#calculator tool

@tool
def add_number(a: float, b: float) -> float:
    """Add two number."""
    return a+b

#multiplication tool
@tool
def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a*b

#knowledge search
@tool
def search_knowledge(query: str) -> str:
    """Search the local knowledge base."""

    knowledge = {
        "langchain": "LangChain is an LLM application framework.",
        "rag": "RAG retrieves relevant documents before generation.",
        "agents": "Agents use models and tools in an execution loop."
    }

    query = query.lower()

    for key, value in knowledge.items():
        if key in query:
            return value

    return "No relevant knowledge found."

#inintialize model
model = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)

#create agent
agent = create_agent(
    model=model,
    tools=[
        add_number,
        multiply_numbers,
        search_knowledge
    ],
    system_prompt=(
        "You are a helpful AI research assistant. "
        "Use tools when calculations or knowledge lookup are needed. "
        "Never invent tool results."
    )
)

#run agent
response = agent.invoke({
    "message":[
        {
            "role":"user",
            "content":"What is RAG? Also calculate 250 multiplied by 40"
        }
    ]
})

print(response["message"][-1].content)