from langchain.agents import AgentState
from pydantic import BaseModel, Field


class Summary(BaseModel):
    summary: str = Field(
        max_length=20000,
        description="A summary of the blog post, maximum 20000 characters",
    )


class Tweets(BaseModel):
    tweets: list[str] = Field(
        max_length=7, description="A list of tweets, maximum 7 tweets"
    )


class TweetAgentState(AgentState):
    """State for the tweet agent."""

    blog_content: str
