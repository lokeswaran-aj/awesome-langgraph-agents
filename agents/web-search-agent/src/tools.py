from langchain_core.tools import tool
from tavily import TavilyClient
import os
from src.prompt import TAVILY_SEARCH_TOOL_DESCRIPTION, SERPER_SEARCH_TOOL_DESCRIPTION
from langchain_community.utilities import GoogleSerperAPIWrapper


_tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


@tool("tavily_search_tool", description=TAVILY_SEARCH_TOOL_DESCRIPTION)
def tavily_search_tool(query: str) -> str:

    try:
        response = _tavily_client.search(query=query, max_results=10)

        results = []
        for idx, result in enumerate(response.get("results", []), 1):
            title = result.get("title", "No title")
            url = result.get("url", "No URL")
            content = result.get("content", "No content")
            results.append(f"{idx}. {title}\n   URL: {url}\n  Result: {content}\n")

        return "\n".join(results) if results else "No results found."
    except Exception as e:
        return f"Error performing search: {str(e)}"


@tool("serper_search_tool", description=SERPER_SEARCH_TOOL_DESCRIPTION)
def serper_search_tool(query: str) -> str:
    search = GoogleSerperAPIWrapper()
    return search.run(query)
