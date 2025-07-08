# utils/arxiv_search.py
import feedparser
import urllib.parse

def search_arxiv(query: str, max_results: int = 5):
    """
    Query the arXiv API and return a list of papers.
    Each entry is a dict with title, authors, summary, and link.
    """
    # 1) Base must include the full domain
    base_url = "http://export.arxiv.org/api/query?"
    
    # 2) URL-encode the query (spaces → %20, etc.)
    encoded_q = urllib.parse.quote(query)
    
    # 3) Build the final URL
    url = (
        f"{base_url}"
        f"search_query=all:{encoded_q}"
        f"&start=0"
        f"&max_results={max_results}"
    )

    # 4) Let feedparser fetch & parse it
    feed = feedparser.parse(url)

    papers = []
    for e in feed.entries:
        papers.append({
            "title":   e.title,
            "authors": [a.name for a in e.authors],
            "summary": e.summary,
            "link":    e.link
        })
    return papers
