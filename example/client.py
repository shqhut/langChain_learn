from langchain.schema.runnable import RunnableMap
from langchain_core.prompts import ChatPromptTemplate
from langserve import RemoteRunnable

openai = RemoteRunnable("http://localhost:8000/openai/")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个喜欢写故事的助手"),
        ("system", "写一个故事，主题是：{topic}")
    ]
)

# 可以自定义链
chain = prompt | RunnableMap(
    {
        "openai": openai
    }
)

response = chain.batch([
    {"topic": "猫"}
])

print(response)