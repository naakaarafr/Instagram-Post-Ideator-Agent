import os
import json
import requests
import time
from crewai_tools import tool
from crewai import Agent, Task, Crew
from langchain_google_genai import ChatGoogleGenerativeAI


class BrowserTools:
    @staticmethod
    @tool("Scrape website content")
    def scrape_and_summarize_website(website: str) -> str:
        """Useful to scrape and summarize a website content, just pass a string with
        only the full url, no need for a final slash `/`, eg: https://google.com or https://clearbit.com/about-us"""
        try:
            # Use Serper's web scraping endpoint
            url = "https://scrape.serper.dev"
            payload = json.dumps({"url": website})
            headers = {
                'X-API-KEY': os.environ.get('SERPER_API_KEY'),
                'Content-Type': 'application/json'
            }
            
            response = requests.post(url, headers=headers, data=payload, timeout=30)
            response.raise_for_status()
            
            # Extract content from Serper response
            scrape_data = response.json()
            content = scrape_data.get('text', '')
            
            if not content:
                return f"No content found for website: {website}"
            
            # DRASTICALLY reduce content to minimize API usage
            content = content[:3000]  # Further reduced from 8000
            
            # Simple text processing instead of using LLM for summarization
            # This eliminates the extra API call that was causing quota issues
            lines = content.split('\n')
            filtered_lines = []
            
            for line in lines:
                line = line.strip()
                if len(line) > 20 and not line.startswith(('Cookie', 'Privacy', 'Terms', 'Copyright')):
                    filtered_lines.append(line)
            
            # Take only the most relevant lines
            summarized_content = '\n'.join(filtered_lines[:50])  # Limit to 50 lines
            
            return f'\nScraped Content: {summarized_content}\n'
            
        except Exception as e:
            return f"Error scraping website {website}: {str(e)}"


class SearchTools:
    @staticmethod
    @tool("Search internet")
    def search_internet(query: str) -> str:
        """Useful to search the internet about a given topic and return relevant results."""
        return SearchTools.search(query)

    @staticmethod
    @tool("Search instagram")
    def search_instagram(query: str) -> str:
        """Useful to search for Instagram posts about a given topic and return relevant results."""
        query = f"site:instagram.com {query}"
        return SearchTools.search(query)

    @staticmethod
    def search(query, n_results=5):
        """Search using Serper API"""
        try:
            url = "https://google.serper.dev/search"
            payload = json.dumps({"q": query})
            headers = {
                'X-API-KEY': os.environ.get('SERPER_API_KEY'),
                'content-type': 'application/json'
            }
            
            # Add delay to respect rate limits
            time.sleep(0.5)
            
            response = requests.post(url, headers=headers, data=payload, timeout=15)
            response.raise_for_status()
            
            results = response.json().get('organic', [])
            search_results = []
            
            for result in results[:n_results]:
                try:
                    search_results.append('\n'.join([
                        f"Title: {result.get('title', 'N/A')}",
                        f"Link: {result.get('link', 'N/A')}",
                        f"Snippet: {result.get('snippet', 'N/A')}",
                        "\n-----------------"
                    ]))
                except KeyError:
                    continue

            content = '\n'.join(search_results)
            return f"\nSearch result: {content}\n"
            
        except Exception as e:
            return f"Error searching: {str(e)}"


# Available tools list for easy import
available_tools = [
    BrowserTools.scrape_and_summarize_website,
    SearchTools.search_internet,
    SearchTools.search_instagram
]