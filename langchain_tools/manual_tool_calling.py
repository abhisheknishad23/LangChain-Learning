from langchain_openai import ChatOpenAI
from langchain.tools import tool

model = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


model_with_tools = model.bind_tools([multiply])

response = model_with_tools.invoke(
    "What is 25 multiplied by 40?"
)

print(response.tool_calls)