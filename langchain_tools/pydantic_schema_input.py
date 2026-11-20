from pydantic import BaseModel, Field
from langchain.tools import tool


class WeatherInput(BaseModel):
    city: str = Field(
        description="City name"
    )

    unit: str = Field(
        default="celsius",
        description="Temperature unit"
    )


@tool(args_schema=WeatherInput)
def get_weather(city: str, unit: str = "celsius") -> str:
    """Get weather information for a city."""

    if unit not in ["celsius", "fahrenheit"]:
        raise ValueError("Unsupported temperature unit")

    return f"Weather information for {city} is unavailable in this demo."