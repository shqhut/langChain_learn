from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_deepseek import ChatDeepSeek

model = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key="sk-d22226a05c3e4918a636bd004472b59e",
    # other params...
)

tools = [TavilySearchResults(max_results = 1)]