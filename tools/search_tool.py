from langchain_core.tools import tool
from pydantic import BaseModel, Field
from tavily import TavilyClient as wc

from config import TAVILY_API_KEY

# topic="finance",
# search_depth="advanced",
# to be included


class SearchQuery(BaseModel):
    query: str = Field(description="Query to search over internet")


@tool(args_schema=SearchQuery)
def search_tool(query: str) -> str:
    """This tool is used for searching over the internet and provide documents in list"""
    try:
        tavily_client = wc(api_key=TAVILY_API_KEY)
        res = tavily_client.search(query, search_depth="advanced", max_results=4)
        top_searches = res["results"][:3]
        return top_searches
    except Exception:
        return "There was some network or other issue , so can't search on internet,tell the user to try again."
