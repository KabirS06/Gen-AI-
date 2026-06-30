from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

#which LLM to use:
llm=HuggingFaceEndpoint(model='meta-llama/Llama-3.1-8B-Instruct',
                          task='text_generation')

model=ChatHuggingFace(llm=llm)

while True:
    user_input=input('You: ')
    if user_input=='exit' : 
        break
    result=model.invoke(user_input)
    print("Morgan : " , result.content)