# utils/llm_agent.py
import os
import google.generativeai as genai
from langchain.agents import initialize_agent, Tool
from langchain.llms.base import LLM

# configure via API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class GemmaLLM(LLM):
    @property
    def _llm_type(self) -> str:
        return "gemma-3-27b-it"

    def _call(self, prompt: str, stop=None) -> str:
        resp = genai.chat.completions.create(
            model="gemma-3-27b-it",
            prompt=[{"author": "user", "content": prompt}],
            temperature=0.7,
            candidate_count=1,
        )
        # most recent versions return .choices
        # if you get an AttributeError, try resp.candidates[0].content
        return resp.choices[0].message.content  

# wrap your DuckDuckGo search
from utils.web_search import web_search
tools = [
    Tool(
        name="WebSearch",
        func=web_search,
        description="Use this to look up web pages & snippets"
    )
]

# initialize the agent
agent = initialize_agent(
    tools=tools,
    llm=GemmaLLM(),
    agent="zero-shot-react-description",
    verbose=False
)
