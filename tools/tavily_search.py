from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv

load_dotenv()

search = TavilySearchResults(max_results=2)
print(search.invoke("今天上海天气怎么样"))
