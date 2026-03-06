from langchain.agents import create_agent
from langchain_core.messages import HumanMessage, SystemMessage

from config import llm_model
from state import AgentState
from tools.search_tool import search_tool

system_prompt = """
You are a research assistant.

Given a user topic, refine it into clear research queries and use the search_tool to gather relevant information.

Focus on:
- latest research and developments
- key concepts and methods
- challenges or limitations
- important findings

Use the search_tool when external information is needed.
Return the gathered documents and a brief summary.
"""


def research_agent(state: AgentState):
    """Initital agent to transform human message to relevant query and search over internet."""
    research_agent = create_agent(model=llm_model, tools=[search_tool])
    res = research_agent.invoke(
        {"messages": [SystemMessage(system_prompt), HumanMessage(state["topic"])]}
    )
    # print(res["messages"][-2].content, "-----------------------------------------")
    docs = res["messages"][-2].content
    return {"summary": res["messages"][-1].content, "documents": docs}
