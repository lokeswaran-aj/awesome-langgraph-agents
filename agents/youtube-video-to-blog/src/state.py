from langchain.agents import AgentState


class BlogAgentState(AgentState):
    """State for the blog agent."""

    transcript: str
