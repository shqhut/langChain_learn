from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template("Tell me a joke about {topic} and {topic2}")
result = prompt_template.invoke({"topic": "cats", "topic2": "dogs"})
print(result)
