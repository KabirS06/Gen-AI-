from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

#which LLM to use:
llm=HuggingFaceEndpoint(model='meta-llama/Llama-3.1-8B-Instruct',
                          task='text_generation')

model=ChatHuggingFace(llm=llm)

# To maintain Chat History or memory
chat_history=[]

while True:
    user_input=input('You: ')
    chat_history.append(user_input)
    if user_input=='exit' : 
        break
    result=model.invoke(chat_history)
    chat_history.append(result.content)
    print("Morgan : " , result.content)