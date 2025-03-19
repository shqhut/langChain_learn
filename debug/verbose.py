from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_deepseek import ChatDeepSeek
import os

model = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key="sk-d22226a05c3e4918a636bd004472b59e",
    # other params...
)

tools = [TavilySearchResults(max_results=1)]

prompt = ChatPromptTemplate.format_prompt(
    [
        (
            "system", "你是一个得力的助手。"
        ),
        (
            "placeholder", "{chat_history}"
        ),
        (
            "human", "{input}"
        ),
        (
            "placeholder", "{agent_scratchpad}"
        )
    ]
)

# 构建工具代理
agent = create_tool_calling_agent(model, tools, prompt)

# 通过传入代理和工具来创建dialing执行器
agent_executor = AgentExecutor(agent=agent, tools=tools)

agent_executor.invoke(
    {"input": "谁执导了2023年的电影《奥本海默》，他多少岁了？"}
)
