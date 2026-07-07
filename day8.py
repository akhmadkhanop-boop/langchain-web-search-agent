from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain.agents import create_agent
from duckduckgo_search import DDGS
from dotenv import load_dotenv
import os
import logging

# Load environment variables
load_dotenv()

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Search_Agent")

# ===== WEB SEARCH TOOL =====
@tool
def web_search(query: str) -> str:
    """Searches the internet for information and returns the results."""
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=3)
        answer = ""
        for r in results:
            answer += f"- {r['title']}: {r['body']}\n"
        return answer

# ===== AI (Brain) =====
llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY"))

# ===== SYSTEM PROMPT =====
system_prompt = """You are an expert AI Assistant.
ALWAYS use the 'web_search' tool to answer questions about current events or facts.
Never rely on your internal memory for factual data; strictly trust the internet search results.
Provide clear and concise answers in English."""

# ===== AGENT =====
agent = create_agent(llm, [web_search], system_prompt=system_prompt)

# ===== HELPER FUNCTION =====
def process_query(question):
    try:
        # Fixed the logger formatting here
        logger.info(f"Question received: {question}")
        result = agent.invoke({"messages": [("user", question)]})
        final_answer = result["messages"][-1].content
        return final_answer
    except Exception as e:
        logger.error(f"Danger Alert - Error: {e}")
        return "System is busy or internet is disconnected. Please try again later."

# ===== EXECUTION =====
question = "Who is the current president of Pakistan?"
answer = process_query(question)

print("\nFINAL ANSWER:")
print(answer)