from langchain.tools import tool

@tool
def multiply(a: int, b:int) -> int:
    """Multiply two integers and return the result."""
    return a*b

result = multiply.invoke({
    "a":250,
    "b":40
})

print(result)