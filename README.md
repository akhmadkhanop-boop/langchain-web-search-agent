# 🌐 Autonomous Web Search AI Agent

A smart and autonomous AI Agent built using Python, LangChain, and the Groq API (Llama 3). Unlike standard LLMs that rely on outdated training data, this agent uses **DuckDuckGo Search** to browse the live internet and provide accurate, up-to-date information.

## 🌟 Features
* **Live Web Search:** Uses the `duckduckgo-search` library to fetch real-time data from the internet.
* **Strict System Prompting:** Forces the AI to rely ONLY on live search results to avoid hallucinations.
* **High Performance:** Powered by Groq's lightning-fast `llama-3.3-70b-versatile` model.
* **Error Handling:** Built-in `try/except` blocks for safe execution.
* **System Logging:** Keeps a detailed backend log of user queries and tool executions.

## 🛠️ Prerequisites
Make sure you have Python installed, then install the required libraries:
```bash
pip install langchain langchain-groq duckduckgo-search python-dotenv
