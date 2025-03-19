from langchain_core.prompts import ChatPromptTemplate

# 传入一个字典类型的对话
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    ("user", "Tell me a joke about {topic}")
])
result = prompt_template.invoke({"topic": "cats"})
print(result)
