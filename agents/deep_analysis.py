from langchain.agents import create_agent
from langchain_core.messages import SystemMessage
from langchain_core.messages.human import HumanMessage

from config import llm_model
from state import AgentState

analysis_system_prompt = """
You are a deep analysis agent.

Input:
- Retrieved documents
- A preliminary summary

Tasks:
1. Verify the summary using the documents.
2. Identify important insights and evidence.
3. Resolve contradictions between sources.
4. Improve or correct the summary if needed.
5. Produce a clear evidence-based analysis.

Use only information from the documents.

Output format:
Final Analysis
- Core Insights
- Key Evidence
- Additional Information
- Conclusion
"""


def deep_analysis_agent(state: AgentState):
    """This is deep analysis agent"""
    analysis_agent = create_agent(model=llm_model)
    context = (
        f"""searched documents: {state["documents"]} ,summary:{state["summary"]}"""
    )
    payload = {
        "messages": [SystemMessage(analysis_system_prompt), HumanMessage(context)]
    }
    res = analysis_agent.invoke(payload)
    return {"insights": res["messages"][-1].content}
