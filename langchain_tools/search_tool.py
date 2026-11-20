from langchain.tools import tool

@tool
def search_information(query:str) -> str:
    """Search a local knowledge base for relevant information."""

    knowledge = {
        "langchain": "LangChain helps developers build LLM applications.",
        "rag": "RAG combines document retrieval with LLM generation.",
        "agent": "AI agents use tools to perform tasks."
    }

    query = query.lower()

    for key, value in knowledge.items():
        if key in query:
            return value

    return "No matching information found"

print(search_information.invoke({
    "query":"Explain RAG"
}))