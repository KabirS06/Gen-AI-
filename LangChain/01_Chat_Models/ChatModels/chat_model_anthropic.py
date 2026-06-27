from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model=ChatAnthropic(model='claude-sonnet-4-6')

result=model.invoke("write a python program to add two input numbers")

print(result.content)
