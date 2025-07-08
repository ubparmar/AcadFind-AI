# utils/web_search.py
from duckduckgo_search import DDGS

def web_search(query: str, max_results: int = 5):
    """
    Run a DuckDuckGo search and return a list of dicts:
    { "title": ..., "href": ..., "body": ... }
    """
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            results.append({
                "title": r.get("title", ""),
                "href":  r.get("href", ""),
                "body":  r.get("body", "")
            })
    return results
