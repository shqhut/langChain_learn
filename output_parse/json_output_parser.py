from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI(model="gpt-4o", temperature=0)


# 定义您期望的数据结构
class Joke(BaseModel):
    setup: str = Field(description="设置笑话的问题")
    punchline: str = Field(description="解决笑话的答案")


# 还有一个用于提示语言模型填充数据结构的查询意图
joke_query = "告诉我一个笑话。"

# 设置解析器
parser = JsonOutputParser(pydantic_object=Joke)

# 设置提示词模版
prompt = PromptTemplate(
    template="回答用户的查询。\n{format_instructions} \n{query} \n",
    input_variables={"query"},
    partial_variables={"format_instructions": parser.get_format_instructions()},
)
print(parser.get_format_instructions())
chain = prompt | model | parser
response = chain.invoke({"query": joke_query})
print(response)
