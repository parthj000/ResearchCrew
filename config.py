import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY") or ""
GROQ_MODEL_NAME = os.getenv("GROQ_MODEL_NAME") or "llama-3.1-8b-instant"
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY") or ""

llm_model = ChatGroq(
    model=GROQ_MODEL_NAME,
    max_retries=2,
    temperature=0.5,
    api_key=GROQ_API_KEY,
)
