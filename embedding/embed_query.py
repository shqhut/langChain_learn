from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding_model = OpenAIEmbeddings()

embedding_query = embedding_model.embed_query("对话中提到的名字是什么")

print(embedding_query[:5])

