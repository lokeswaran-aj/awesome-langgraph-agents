import asyncio
import ast
from typing import Annotated
from langchain.tools import InjectedToolCallId, tool
from langchain_mcp_adapters.client import MultiServerMCPClient
from klavis import Klavis
from klavis.types import McpServerName
import os
from langgraph.types import Command
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage
from src.model import model
from src.prompt import BLOG_POST_GENERATOR_SYSTEM_PROMPT
from langgraph.graph.state import END
from src.state import BlogAgentState

klavis_client = Klavis(api_key=os.getenv("KLAVIS_API_KEY"))

response = klavis_client.mcp_server.create_server_instance(
    server_name=McpServerName.YOUTUBE, user_id="youtube-video-to-blog"
)
mcp_client = MultiServerMCPClient(
    {"youtube": {"transport": "streamable_http", "url": response.server_url}}
)

youtube_tools = asyncio.run(mcp_client.get_tools())


@tool(
    "get_youtube_video_transcript",
    description="Returns the transcript of a YouTube video by its URL",
)
async def get_youtube_video_transcript(
    url: str, tool_call_id: Annotated[str, InjectedToolCallId]
) -> Command:
    mcp_tool = [t for t in youtube_tools if t.name == "get_youtube_video_transcript"][0]

    result = await mcp_tool.ainvoke({"url": url})
    result_dict = ast.literal_eval(result)
    transcript = result_dict.get("transcript", [])

    transcript_text = " ".join(segment.get("text", "") for segment in transcript)

    return Command(
        update={
            "messages": [
                ToolMessage(
                    content=transcript_text,
                    tool_call_id=tool_call_id,
                )
            ],
            "transcript": transcript_text,
        },
    )


def blog_post_generator(state: BlogAgentState) -> Command:
    system_message = SystemMessage(BLOG_POST_GENERATOR_SYSTEM_PROMPT)

    transcript = state["transcript"]

    messages = [system_message, HumanMessage(transcript)]
    response = model.invoke(messages)
    return Command(
        goto=END,
        update={
            "messages": [
                AIMessage(
                    content=response.content,
                )
            ],
        },
    )
