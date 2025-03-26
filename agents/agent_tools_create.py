from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from langchain.tools.retriever import create_retriever_tool
from langchain_deepseek import ChatDeepSeek
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain import hub
from langchain.agents import create_tool_calling_agent,AgentExecutor
from langchain.globals import set_verbose


load_dotenv()

model = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key="sk-d22226a05c3e4918a636bd004472b59e",
    # other params...
)

loader = WebBaseLoader("https://zh.wikipedia.org/wiki/%E7%8C%AB")
docs = loader.load()
documents = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200).split_documents(docs)
vector = FAISS.from_documents(documents, OpenAIEmbeddings())
retriever = vector.as_retriever()

# result = retriever.invoke("猫的特征")[0]
# print(result)

retriever_tool = create_retriever_tool(retriever, "wiki_search", "搜索维基百科")
search = TavilySearchResults(max_results=1)

tools = [search, retriever_tool]

prompt = hub.pull("hwchase17/openai-functions-agent")

agent = create_tool_calling_agent(model, tools, prompt)

set_verbose(True)
agent_executor = AgentExecutor(agent=agent, tools=tools)


print(agent_executor.invoke({"input": "猫的特征？今天上海天气怎么样？"}))

