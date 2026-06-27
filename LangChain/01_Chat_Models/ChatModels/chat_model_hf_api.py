from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint # to use hf's API
from dotenv import load_dotenv
import os


load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task='text-generation'
)

model=ChatHuggingFace(llm=llm)

result=model.invoke("write a python program to add two number")

print(result.content)
