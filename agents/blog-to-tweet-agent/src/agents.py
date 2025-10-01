from langchain_core.messages import SystemMessage
from src.state import TweetAgentState
from src.model import model
from langchain.agents import create_agent
from src.prompt import (
    SUPERVISOR_AGENT_SYSTEM_PROMPT,
)
from src.tools import tools


system_message = SystemMessage(SUPERVISOR_AGENT_SYSTEM_PROMPT)

supervisor_agent = create_agent(
    name="supervisor_agent",
    model=model,
    prompt=system_message,
    state_schema=TweetAgentState,
    tools=tools,
)
