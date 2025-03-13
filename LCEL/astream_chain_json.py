# 创建 DeepSeek 的 LLM 实例
from langchain_deepseek import ChatDeepSeek
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
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

parser = StrOutputParser()

chain = (
        model | JsonOutputParser()
)


async def async_stream():
    async for text in chain.astream(
            "以JSON格式输出法国、西班牙和日本的国际及其人口列表。"
            '使用一个带有"countries"外部键的字典，其中包含国家列表。'
            "每个国家都应该有键'name'和'population'"
    ):
        print(text, flush=True)

# 运行异步流处理
asyncio.run(async_stream())