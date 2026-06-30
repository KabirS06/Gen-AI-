from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain.messages import AIMessage , SystemMessage , HumanMessage

load_dotenv()

#which LLM to use:
llm=HuggingFaceEndpoint(model='meta-llama/Llama-3.1-8B-Instruct',
                          task='text_generation')

model=ChatHuggingFace(llm=llm)

# To maintain Chat History or memory
chat_history=[SystemMessage(content="You are a helpful Assistant")]


while True:
    user_input=input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input=='exit' : 
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("Morgan : " , result.content)
print (chat_history)