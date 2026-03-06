# ResearchCrew

ResearchCrew is a **multi-agent AI research system** built using **LangGraph and LangChain**.  
It autonomously researches a topic, analyzes gathered information, and generates a structured report.  
The system also supports **tool usage, agent orchestration, and extensible knowledge workflows**.

---
<img width="1898" height="921" alt="image" src="https://github.com/user-attachments/assets/fedb1101-3912-4d24-a5ee-67b080f2ac60" />


## Overview

ResearchCrew demonstrates how **multiple AI agents can collaborate** to perform complex tasks such as research and analysis.

Instead of relying on a single LLM call, the system decomposes the problem into specialized agents:

1. **Research Agent** – searches the web and collects relevant documents  
2. **Analysis Agent** – extracts insights from gathered information  
3. **Report Agent** – synthesizes insights into a structured research report  

These agents are orchestrated using **LangGraph**, enabling modular and extensible workflows.

---

## Architecture


User Topic
↓
Research Agent
↓
Web Search Tool
↓
Documents
↓
Analysis Agent
↓
Insights
↓
Report Agent
↓
Structured Research Report


LangGraph manages the **workflow state** and coordinates communication between agents.

---

## Features

- Multi-agent orchestration using **LangGraph**
- Tool calling via **LangChain Structured Tools**
- Automated research and insight extraction
- Modular agent architecture
- Extensible for RAG and knowledge base systems
- Easily integrable with web interfaces (Streamlit / APIs)

---

## Tech Stack

- **Python**
- **LangGraph**
- **LangChain**
- **Groq LLM API**
- **Structured Tools**
- **dotenv for environment management**

---

## Project Structure


ResearchCrew/

core/
config.py

agents/
research_agent.py
analysis_agent.py
report_agent.py

tools/
search_tool.py
email_tool.py

graph/
research_graph.py

main_agent.py


---

## Installation

Clone the repository:


git clone https://github.com/yourusername/researchcrew.git

cd researchcrew


Create a virtual environment:


python -m venv venv
source venv/bin/activate

Windows

venv\Scripts\activate


Install dependencies:


pip install -r requirements.txt


---

## Environment Variables

Create a `.env` file in the root directory:


GROQ_API_KEY=your_groq_api_key


---

## Usage

Run the app:


streamlit run app.py


Example input topic:


"Large Language Model research papers"


The system will:

1. Search the internet for relevant information
2. Extract key insights
3. Generate a structured research report

---

## Example Workflow


User: Research LLM research papers

Research Agent
↓
Web Search Tool

Analysis Agent
↓
Extract insights

Report Agent
↓
Generate final report


---

## Future Improvements

- Retrieval-Augmented Generation (RAG)
- Vector database integration
- Knowledge base expansion

---

## Why Multi-Agent Systems?

Complex tasks like research require multiple reasoning steps.  
Instead of one large prompt, ResearchCrew separates responsibilities between specialized agents.

Benefits include:

- Better reasoning quality
- Modular architecture
- Easier debugging
- Scalable workflows

---

## License

MIT License

---

## Author

Parth Joshi
