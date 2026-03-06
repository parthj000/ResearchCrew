from langgraph.graph import END, StateGraph

from agents.deep_analysis import deep_analysis_agent
from agents.generate_report import generate_report_agent
from agents.research_agent import research_agent
from state import AgentState


class ResearchGraph:
    def __init__(self):
        graph = StateGraph(AgentState)
        graph.add_node("research", research_agent)
        graph.add_node("deep_analysis", deep_analysis_agent)
        graph.add_node("report_gen", generate_report_agent)
        graph.add_edge("research", "deep_analysis")
        graph.add_edge("deep_analysis", "report_gen")
        graph.add_edge("report_gen", END)
        graph.set_entry_point("research")
        self.graph = graph.compile()

    def generate_initial_state(self, query: str):
        state: AgentState = {
            "documents": [],
            "topic": query,
            "insights": "",
            "summary": "",
        }
        return state
