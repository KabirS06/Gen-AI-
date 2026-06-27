from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # load .env file and connect API key

llm=OpenAI(model='gpt-3.5-turbo-instruct') # model name 

result=llm.invoke("what is the value of pi till the 10th decimal value") # return the result of the query

print(result)
