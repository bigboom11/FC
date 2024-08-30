# from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.ollama import Ollama

# 初始化 Ollama LLM 客户端
ollama_llm = Ollama(base_url=os.getenv('OLLAMA_BASE_URL'), model="llama3")

# 加载文档
# documents = SimpleDirectoryReader("./data").load_data()

# 创建索引并使用 Ollama LLM
# index = GPTVectorStoreIndex(documents, llm=ollama_llm)

# # 执行查询
# response = index.query("Summarize the key points of the documents.", temperature=0.5, max_tokens=500)
# print(response)

