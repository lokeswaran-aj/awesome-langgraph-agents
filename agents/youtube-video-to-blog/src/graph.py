from langchain.agents import ToolNode
from langchain.tools.tool_node import tools_condition
from langchain_core.messages import SystemMessage
from langgraph.graph.message import MessagesState
from langgraph.graph.state import StateGraph, START, END
from src.model import model
from src.prompt import (
    YOUTUBE_VIDEO_TO_BLOG_AGENT_SYSTEM_PROMPT,
)
from src.tools import blog_post_generator, get_youtube_video_transcript
from src.state import BlogAgentState


def youtube_video_to_blog_agent(state: BlogAgentState):
    system_message = SystemMessage(YOUTUBE_VIDEO_TO_BLOG_AGENT_SYSTEM_PROMPT)
    llm_with_tool = model.bind_tools([get_youtube_video_transcript])
    messages = [system_message] + state["messages"]
    response = llm_with_tool.invoke(messages)
    return {
        "messages": [response],
    }


graph = StateGraph(BlogAgentState, input_schema=MessagesState)

graph.add_node("youtube_video_to_blog_agent", youtube_video_to_blog_agent)
graph.add_node("get_youtube_video_transcript", ToolNode([get_youtube_video_transcript]))
graph.add_node("blog_post_generator", blog_post_generator)

graph.add_edge(START, "youtube_video_to_blog_agent")
graph.add_conditional_edges(
    "youtube_video_to_blog_agent",
    tools_condition,
    {"tools": "get_youtube_video_transcript", END: END},
)
graph.add_edge("get_youtube_video_transcript", "blog_post_generator")
graph.add_edge("blog_post_generator", END)

app = graph.compile(name="youtube-video-to-blog-agent")
