from typing import Annotated
from operator import add
from typing_extensions import TypedDict


class State(TypedDict):

    results: Annotated[list[str], add]