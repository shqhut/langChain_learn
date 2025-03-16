# 创建 DeepSeek 的 LLM 实例
from langchain_deepseek import ChatDeepSeek
import asyncio

model = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key="sk-d22226a05c3e4918a636bd004472b59e",
    # other params...
)

# 异步流处理
async def async_stream():
    events = []
    async for event in model.astream_events(input="hello", version="v2"):
        events.append(event)
    print(events)

# 运行异步流处理
asyncio.run(async_stream())
