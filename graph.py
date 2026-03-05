import operator
from typing import Annotated, TypedDict

from langchain_core.messages import (
    AnyMessage,
    SystemMessage,
    ToolMessage,
)
from langgraph.graph import END, StateGraph


class AgentState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]


class Agent:
    def __init__(self, model, tools: list, system_prompt: str):
        self.system_prompt = system_prompt

        graph = StateGraph(AgentState)
        graph.add_node("llm", self.llm_call)
        graph.add_node("tool_call", self.execute_tool)
        graph.add_conditional_edges(
            "llm", self.decide_tool_calling, {True: "tool_call", False: END}
        )
        graph.add_edge("tool_call", "llm")

        graph.set_entry_point("llm")

        self.graph = graph.compile()
        self.tools = {t.name: t for t in tools}
        print(self.tools)
        self.model = model.bind_tools(tools)

    def llm_call(self, state: AgentState):
        """Primary search node, Calling the llm"""
        messages = state["messages"]
        if self.system_prompt:
            messages = [SystemMessage(self.system_prompt)] + messages
        response = self.model.invoke(messages)
        return {"messages": [response]}

    def execute_tool(self, state: AgentState):
        """Node which execute the tool"""
        tools = state["messages"][-1].tool_calls
        results = []
        for t in tools:
            # now execute each tool and return the tool message
            if t["name"] not in self.tools:
                t_message = "Error: no such tool found in inventory"
            else:
                t_message = self.tools[t["name"]].invoke(t["args"])
            results.append(
                ToolMessage(
                    content=str(t_message), name=t["name"], tool_call_id=t["id"]
                )
            )
        return {"messages": results}

    def decide_tool_calling(self, state: AgentState):
        """Function which decides if the tool should be called or not"""
        is_tool_req = len(state["messages"][-1].tool_calls)
        return is_tool_req > 0
