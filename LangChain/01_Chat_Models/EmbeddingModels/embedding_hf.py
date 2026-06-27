from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding=HuggingFaceEmbeddings(model_name='sentence-transformers/all-mpnet-base-v2')

text="Delhi is the capital of India"

result=embedding.embed_query(text)

print(str(result))