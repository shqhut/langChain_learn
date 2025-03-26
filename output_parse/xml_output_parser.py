from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import XMLOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI(model="gpt-4o", temperature=0)

# 还有一个用于提示语言模型填充数据结构的查询意图
actor_query = "生成周星驰的简化电影作品列表，按照最新的时间降序，电影名称用中文"
# 设置解析器 + 将提示词注入提示模版
parser = XMLOutputParser(tags=["movies", "actor", "film", "name", "genre"])
# parser = XMLOutputParser()
print(parser.get_format_instructions())
"""
input_variables和partial_variables
"""
prompt = PromptTemplate(
    template="回答用户的查询。\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = prompt | model
response = chain.invoke({"query": actor_query})
# xml_output = parser.parse(response.content)
print(response.content)
# print(xml_output)

