from langgraph.graph import END, START, StateGraph

from src.state import TweetAgentState
from src.agents import supervisor_agent


graph_builder = StateGraph(TweetAgentState)

graph_builder.add_node("supervisor_agent", supervisor_agent)

graph_builder.add_edge(START, "supervisor_agent")
graph_builder.add_edge("supervisor_agent", END)

app = graph_builder.compile(name="blog-to-tweet-agent")
