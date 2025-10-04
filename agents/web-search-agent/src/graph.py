from langchain.agents import AgentState
from langgraph.graph import END, START, StateGraph

from src.agents import web_search_agent


graph_builder = StateGraph(AgentState)

graph_builder.add_node("web_search_agent", web_search_agent)

graph_builder.add_edge(START, "web_search_agent")
graph_builder.add_edge("web_search_agent", END)

app = graph_builder.compile(name="web-search-agent")
