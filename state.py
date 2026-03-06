from typing import TypedDict


class AgentState(TypedDict):
    documents: list
    topic: str | None
    insights: str
    summary: str
