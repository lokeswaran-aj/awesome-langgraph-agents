from langchain_anthropic import ChatAnthropic
import os

model = ChatAnthropic(model="claude-sonnet-4-5", api_key=os.getenv("ANTHROPIC_API_KEY"))
