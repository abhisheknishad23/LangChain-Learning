from collections.abc import Callable

from langchain.agents.middleware import wrap_tool_call
from langchain.messages import ToolMessage
from langchain.tools.tool_node import ToolCallRequest

@wrap_tool_call
def handle_tool_errors(
    request: ToolCallRequest,
    handler:Callable
) -> ToolMessage:
    
    try:
        return handler(request)
    except (ValueError, KeyError,ZeroDivisionError) as error:
        return ToolMessage(
            content= f"Tool failed: {error}",
            tool_call_id = request.tool_call["id"]
        )