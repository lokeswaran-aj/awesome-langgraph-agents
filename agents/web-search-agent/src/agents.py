from langchain_core.messages import SystemMessage
from datetime import datetime
from src.model import model
from langchain.agents import AgentState, create_agent
from src.prompt import (
    WEB_SEARCH_AGENT_SYSTEM_PROMPT,
)
from src.tools import tavily_search_tool, serper_search_tool

tools = [tavily_search_tool, serper_search_tool]

system_message = SystemMessage(
    WEB_SEARCH_AGENT_SYSTEM_PROMPT.format(
        current_date_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
)

web_search_agent = create_agent(
    name="web_search_agent",
    model=model,
    prompt=system_message,
    state_schema=AgentState,
    tools=tools,
)
