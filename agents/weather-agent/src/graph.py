from langgraph.graph import END, START, MessagesState, StateGraph

from src.agents import weather_agent


graph_builder = StateGraph(MessagesState)

graph_builder.add_node("weather_agent", weather_agent)

graph_builder.add_edge(START, "weather_agent")
graph_builder.add_edge("weather_agent", END)

app = graph_builder.compile(name="weather-agent")
