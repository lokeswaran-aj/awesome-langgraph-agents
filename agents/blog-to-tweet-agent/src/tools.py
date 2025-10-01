import os
from langchain_community.document_loaders.firecrawl import FireCrawlLoader
from typing import Annotated

from langchain.tools.tool_node import InjectedState
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from langchain_core.tools import tool, InjectedToolCallId
from langgraph.types import Command
from src.state import Summary, Tweets
from src.model import model
from src.prompt import (
    BLOG_POST_URL_TO_SUMMARY_TOOL_NAME,
    BLOG_POST_URL_TO_SUMMARY_TOOL_DESCRIPTION,
    TWEET_THREAD_GENERATOR_TOOL_NAME,
    TWEET_THREAD_GENERATOR_TOOL_DESCRIPTION,
    BLOG_SUMMARIZATION_SYSTEM_PROMPT,
    TWEET_THREAD_GENERATION_SYSTEM_PROMPT,
)


@tool(
    BLOG_POST_URL_TO_SUMMARY_TOOL_NAME,
    description=BLOG_POST_URL_TO_SUMMARY_TOOL_DESCRIPTION,
)
def crawl_and_summarize_blog(
    url: str,
    state: Annotated[dict, InjectedState],
    tool_call_id: Annotated[str, InjectedToolCallId],
) -> Command:

    firecrawl_loader = FireCrawlLoader(
        api_key=os.getenv("FIRECRAWL_API_KEY"),
        url=url,
        mode="crawl",
        params={"limit": 1},
    )
    blog_content = firecrawl_loader.load()

    if len(blog_content[0].page_content) > 50000:
        system_message = SystemMessage(BLOG_SUMMARIZATION_SYSTEM_PROMPT)
        messages = [system_message, HumanMessage(content=blog_content[0].page_content)]
        llm_with_structured_output = model.with_structured_output(Summary)
        response = llm_with_structured_output.invoke(messages)
        blog_content = response.summary
    else:
        blog_content = blog_content[0].page_content

    return Command(
        update={
            "blog_content": blog_content,
            "messages": [
                ToolMessage(
                    content="Here is the content of the blog post: " + blog_content,
                    tool_call_id=tool_call_id,
                )
            ],
        }
    )


@tool(
    TWEET_THREAD_GENERATOR_TOOL_NAME,
    description=TWEET_THREAD_GENERATOR_TOOL_DESCRIPTION,
)
def generate_tweet_thread(
    current_messages: Annotated[list, InjectedState("messages")],
    tool_call_id: Annotated[str, InjectedToolCallId],
) -> Command:
    llm_with_structured_output = model.with_structured_output(Tweets)
    system_message = SystemMessage(TWEET_THREAD_GENERATION_SYSTEM_PROMPT)
    messages = [system_message] + current_messages[:-1]
    response = llm_with_structured_output.invoke(messages)
    generated_tweets = response.tweets

    return Command(
        update={
            "messages": [
                ToolMessage(
                    content="Here are the generated tweets: \n\n"
                    + "\n".join(generated_tweets),
                    tool_call_id=tool_call_id,
                ),
            ],
        },
    )


tools = [crawl_and_summarize_blog, generate_tweet_thread]
