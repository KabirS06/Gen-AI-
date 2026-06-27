from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-35-flash")

result=model.invoke("Write a program to add two numbers in python")

print(result.content)