from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
# 创建 DeepSeek 的 LLM 实例
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

messages = [
    SystemMessage(content="将以下内容从英文翻译成中文"),
    HumanMessage(content="It's a nice day today")
]

parser = StrOutputParser()
result = model.invoke(messages)
print(result)
response = parser.invoke(result)
print(response)
