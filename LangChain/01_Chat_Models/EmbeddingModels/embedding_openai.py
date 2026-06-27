from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large', dimension=32) #convert to 31 dimension vector 

#result=embedding.embed_query("Delhi is the capital of India")

documents=["Delhi is the capital of India",
           "Beijing is the capital of China",
           "Tokyo is the capital of Japan"
           ]

result =embedding.embed_documents(documents)
print(str(result))