from langchain.agents import create_agent
from langchain_core.messages import HumanMessage, SystemMessage

from config import llm_model
from state import AgentState

system_prompt = report_system_prompt = """
You are a professional research report generator.

You will receive deep analysis results from a research system.

Your job is to convert the analysis into a well-structured report.

Structure the report using:

# Title

## Executive Summary
A short overview of the findings.

## Key Insights
Important discoveries from the research.

## Detailed Analysis
Expanded explanation of the findings.

## Evidence
Key facts or data supporting the conclusions.

## Final Conclusion
Clear and concise final takeaway.

The report should be:
- Clear
- Professional
- Structured
- Easy to read

Do not repeat raw documents.
Use only the information provided.
"""


def generate_report_agent(state: AgentState):
    """Generate final research report"""
    context = f"""
    Deep Analysis Results:
    {state["insights"]}
    """
    report_agent = create_agent(model=llm_model)
    res = report_agent.invoke(
        {"messages": [SystemMessage(system_prompt), HumanMessage(context)]}
    )
    print(res["messages"][-1].content)
    return {"report": res["messages"][-1].content}
