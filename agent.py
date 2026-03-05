import os
import pprint

from dotenv import load_dotenv
from langchain_core.messages.human import HumanMessage
from langchain_groq import ChatGroq

from email_tool import send_email
from graph import Agent
from tools import execute_search

load_dotenv()


system_prompt = "you are research expert"
model = ChatGroq(
    model=os.getenv("GROQ_MODEL_NAME") or "llama-3.1-8b-instant",
    max_retries=2,
    temperature=0.2,
)
agent = Agent(
    model=model, tools=[execute_search, send_email], system_prompt=system_prompt
)
result = agent.graph.invoke(
    {"messages": [HumanMessage("send email to parth@mmm.com about albert einstein")]}
)

res2 = agent.graph.invoke(
    {
        "messages": [
            HumanMessage(
                "what was the last question i asked and where did you send the mail"
            )
        ]
    }
)


pprint.pprint(result)
pprint.pprint(res2)
