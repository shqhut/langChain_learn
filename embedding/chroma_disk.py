from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

load_dotenv()

# 加载文档，并将其分割成片段
loader = TextLoader("../resource/knowledge.txt", encoding="UTF-8")
documents = loader.load()

# 将其分割成片段
text_splitter = CharacterTextSplitter(chunk_size=1500, chunk_overlap=200)
docs = text_splitter.split_documents(documents)

embedding_model = OpenAIEmbeddings()

# 保存到磁盘
db = Chroma.from_documents(docs, embedding_model, persist_directory="./chroma_db")
# 从磁盘加载
db3 = Chroma(persist_directory="./chroma_db", embedding_function=embedding_model)

target_docs = db3.similarity_search("Pixar公司是做什么的?")

print(len(target_docs))
print(target_docs[0].page_content)
