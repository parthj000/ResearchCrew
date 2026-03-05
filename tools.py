from langchain_core.tools import tool
from pydantic import BaseModel, Field

from main import get_data


class SearchQuery(BaseModel):
    query: str = Field(description="Query to search on internet.")


@tool(args_schema=SearchQuery)
def execute_search(query: str) -> str:
    """
    Search the internet for real-time or factual information.
    Always use this tool when the user asks to search the internet.
    """

    return get_data(query)
