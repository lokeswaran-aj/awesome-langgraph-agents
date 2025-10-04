<div align="center">

# 🤖 Awesome LangGraph Agents

### A curated collection of production-ready AI agents built with LangGraph, LangChain, and Claude

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Latest-green.svg)](https://github.com/langchain-ai/langgraph)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

[🚀 Getting Started](#-getting-started) • [🤖 Agents](#-agents) • [💡 Contributing](#-contributing)

</div>

---

## 📌 Overview

Welcome to **Awesome LangGraph Agents** - a comprehensive collection of sophisticated AI agents built using the latest LangGraph framework. Each agent demonstrates best practices in agentic AI development, featuring multi-step reasoning, tool orchestration, and production-ready architectures.

### Why LangGraph?

- 🔄 **Stateful Workflows**: Build complex, multi-step agent workflows with persistent state
- 🛠️ **Tool Integration**: Seamlessly integrate custom tools and APIs
- 🎯 **Precise Control**: Fine-grained control over agent behavior and decision-making
- 🔍 **Observable**: Built-in support for tracing, debugging, and monitoring
- 🚀 **Production Ready**: Deploy with LangGraph Cloud or self-host

### What You'll Find Here

- ✅ **Production-Ready Agents**: Fully functional, well-documented agents you can deploy today
- ✅ **Best Practices**: Clean code, comprehensive prompts, and robust error handling
- ✅ **Real-World Use Cases**: Practical agents solving actual business problems
- ✅ **Educational**: Learn agent architecture patterns and LangGraph concepts
- ✅ **Open Source**: MIT licensed - use freely in your projects

---

## 🤖 Agents

### Weather & Planning

<table>
<tr>
<td width="50%">

#### 🌤️ [Weather Agent](./agents/weather-agent)

Intelligent weather assistant providing forecasts and activity-based recommendations.

**Key Features:**

- 🎯 Activity-based YES/NO recommendations
- ⏰ Time-aware forecasting (tonight, tomorrow, etc.)
- 📊 Comprehensive weather data (current + 7-day forecast)
- 🆓 Completely FREE - no weather API key needed
- 🤖 Claude Sonnet 4.5 powered analysis

**Tech Stack:** LangGraph • LangChain • Anthropic • Open-Meteo

[View Demo](./agents/weather-agent#demo) | [Documentation](./agents/weather-agent/README.md)

</td>
<td width="50%">
<img src="./agents/weather-agent/assets/weather-agent-demo.gif" alt="Weather Agent Demo" width="100%"/>
</td>
</tr>
</table>

---

### Search & Research

<table>
<tr>
<td width="50%">

#### 🔍 [Web Search Agent](./agents/web-search-agent)

Intelligent search assistant that provides comprehensive, well-researched answers by leveraging multiple web search APIs.

**Key Features:**

- 🔍 Dual search engine integration (Tavily + Google Serper)
- 🎯 Cross-references and validates information across sources
- 📊 Expert-quality responses with source attribution
- ⚡ Real-time information from the web
- 🤖 Claude Sonnet 4.5 powered synthesis

**Tech Stack:** LangGraph • LangChain • Anthropic • Tavily • Serper

[View Demo](./agents/web-search-agent#demo) | [Documentation](./agents/web-search-agent/README.md)

</td>
<td width="50%">
<img src="./agents/web-search-agent/assets/web-search-agent-demo.gif" alt="Web Search Agent Demo" width="100%"/>
</td>
</tr>
</table>

---

### Content & Social Media

<table>
<tr>
<td width="50%">

#### 📱 [Blog to Tweet Agent](./agents/blog-to-tweet-agent)

Automatically converts blog posts into engaging X/Twitter threads.

**Key Features:**

- 🔗 Web scraping with Firecrawl
- 🤖 Smart content summarization
- 🧵 Optimized tweet thread generation
- ✨ Claude Sonnet 4.5 powered

**Tech Stack:** LangGraph • LangChain • Anthropic • Firecrawl

[View Demo](./agents/blog-to-tweet-agent#demo) | [Documentation](./agents/blog-to-tweet-agent/README.md)

</td>
<td width="50%">
<img src="./agents/blog-to-tweet-agent/assets/tweet-generator-demo.gif" alt="Blog to Tweet Demo" width="100%"/>
</td>
</tr>
</table>

---

### Coming Soon 🚧

We're actively developing more agents! Star ⭐ this repo to stay updated.

**Planned Agents:**

- 📧 Email Response Agent - Intelligent email drafting and responses
- 📊 Data Analysis Agent - Automated insights from datasets
- 💬 Customer Support Agent - Multi-turn support conversations

Have an idea? [Open an issue](../../issues/new) or contribute!

---

## 🚀 Getting Started

### Prerequisites

- Python 3.12 or higher
- [uv](https://docs.astral.sh/uv/) (recommended) or pip
- API keys for the services you plan to use (Anthropic, OpenAI, etc.)

### Quick Start

1. **Clone the repository**

```bash
git clone https://github.com/lokeswaran-aj/awesome-langgraph-agents.git
cd awesome-langgraph-agents
```

2. **Choose an agent and navigate to its directory**

```bash
# Weather Agent
cd agents/weather-agent
```

3. **Install dependencies**

```bash
# Using uv (recommended)
uv sync

# Or using pip
pip install -e .
```

4. **Configure environment variables**

```bash
cp .env.example .env
# Edit .env with your API keys
```

5. **Run the agent**

```bash
langgraph dev
```

6. **Access LangGraph Studio**

Open [LangGraph Studio](https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024) in your browser.

---

## 🏗️ Tech Stack

### Core Frameworks

- **[LangGraph](https://github.com/langchain-ai/langgraph)** - Agent workflow orchestration
- **[LangChain](https://github.com/langchain-ai/langchain)** - LLM application framework
- **[Anthropic Claude](https://www.anthropic.com/)** - Advanced AI models

### Common Tools & Integrations

- **Open-Meteo** - Free weather data API
- **Tavily** - AI-optimized search API
- **Google Serper** - Google search results API
- **Firecrawl** - Web scraping and content extraction
- **Python 3.12+** - Modern Python features
- **uv** - Fast Python package management
- **LangSmith** - Observability and debugging

---

## 💡 Contributing

We welcome contributions! Here's how you can help:

### Adding a New Agent

1. **Fork the repository**
2. **Create a new directory** under `agents/your-agent-name/`
3. **Follow the agent template structure**:
   ```
   agents/your-agent-name/
   ├── README.md              # Comprehensive documentation
   ├── langgraph.json         # LangGraph configuration
   ├── pyproject.toml         # Dependencies
   ├── .env.example           # Environment template
   ├── assets/                # Demo videos, images
   └── src/
       ├── __init__.py
       ├── agents.py          # Agent definitions
       ├── graph.py           # LangGraph workflow
       ├── model.py           # LLM configuration
       ├── prompt.py          # All prompts
       ├── state.py           # State schemas
       └── tools.py           # Custom tools
   ```
4. **Include a demo** (GIF or video)
5. **Write comprehensive documentation**
6. **Submit a pull request**

### Contribution Guidelines

- ✅ Write clean, well-documented code
- ✅ Include comprehensive README with usage examples
- ✅ Add demo visuals (GIF/screenshots)
- ✅ Follow existing code style and structure
- ✅ Test thoroughly before submitting
- ✅ Update main README with your agent

### Code Quality Standards

- Use type hints
- Write descriptive docstrings
- Separate prompts into dedicated files
- Include error handling
- Provide environment templates

---

## 📝 Project Structure

```
awesome-langgraph-agents/
├── agents/                    # Individual agent directories
│   ├── weather-agent/        # Weather & planning agent
│   │   ├── README.md
│   │   ├── src/
│   │   └── ...
│   ├── web-search-agent/     # Web search & research agent
│   │   ├── README.md
│   │   ├── src/
│   │   └── ...
│   └── blog-to-tweet-agent/  # Content generation agent
│       ├── README.md
│       ├── src/
│       └── ...
├── LICENSE                    # MIT License
└── README.md                  # This file
```

---

## 🌟 Star History

If you find this project helpful, please consider giving it a ⭐!

[![Star History Chart](https://api.star-history.com/svg?repos=lokeswaran-aj/awesome-langgraph-agents&type=Date)](https://star-history.com/#lokeswaran-aj/awesome-langgraph-agents&Date)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Inspired by [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
- Built with [LangGraph](https://github.com/langchain-ai/langgraph) by LangChain
- Powered by [Anthropic Claude](https://www.anthropic.com/)

---

<div align="center">

### Made with ❤️ by [Lokeswaran Aruljothy](https://lokes.dev)

**[⬆ Back to Top](#-awesome-langgraph-agents)**

</div>
