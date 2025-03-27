from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding_model = OpenAIEmbeddings()

embeddings = embedding_model.embed_documents(
    [
        "嗨！",
        "哦，你好！",
        "你叫什么名字？",
        "我的朋友们叫我World",
        "Hello World！"
    ]
)

print(len(embeddings), len(embeddings[0]))

