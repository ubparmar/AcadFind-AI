# app.py
import os
import streamlit as st
from dotenv import load_dotenv

# load .env keys
load_dotenv()

# Streamlit page config
st.set_page_config(page_title="AcadFind-AI", layout="wide")
st.title("🔍 AcadFind-AI")

# inputs
query = st.text_input("Enter your niche research topic")
ai_q  = st.text_input("Ask the AI agent a follow-up question")

# lazy imports for performance
if query:
    from utils.arxiv_search import search_arxiv
    with st.spinner("📄 Fetching from arXiv…"):
        papers = search_arxiv(query, max_results=5)

    st.markdown("### 📰 arXiv Results")
    for p in papers:
        st.subheader(p["title"])
        st.write("**Authors:**", ", ".join(p["authors"]))
        st.write(p["summary"][:300] + "…")
        st.markdown(f"[Read more]({p['link']})")
        st.markdown("---")

if ai_q:
    from utils.llm_agent import agent
    with st.spinner("🤖 Thinking…"):
        answer = agent.run(ai_q)
    st.markdown("### 💡 AI Agent Answer")
    st.write(answer)
