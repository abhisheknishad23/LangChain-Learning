from langchain.tools import tool, ToolRuntime


@tool
def get_user_preference(
    preference: str,
    runtime: ToolRuntime
) -> str:
    """Retrieve a saved preference from user memory."""

    user_data = runtime.store.get(
        ("user_preferences",),
        preference
    )

    if user_data is None:
        return "No preference saved."

    return str(user_data.value)