from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model="gpt-4",temperature=0, max_completion_tokens=10) #loads model

result=model.invoke("what is the value of pi till the 12th decimal positon") # returns dictionaries of values

print(result.content)