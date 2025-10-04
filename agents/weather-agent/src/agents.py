from langchain_core.messages import SystemMessage
from datetime import datetime
from src.model import model
from langchain.agents import AgentState, create_agent
from src.prompt import (
    WEATHER_AGENT_SYSTEM_PROMPT,
)
from src.tools import tools


system_message = SystemMessage(
    WEATHER_AGENT_SYSTEM_PROMPT.format(
        current_date_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
)

weather_agent = create_agent(
    name="weather_agent",
    model=model,
    prompt=system_message,
    state_schema=AgentState,
    tools=tools,
)
