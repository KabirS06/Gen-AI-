from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain.messages import HumanMessage , SystemMessage
from langchain_core.prompts import ChatPromptTemplate

chat_template=ChatPromptTemplate([
    ('system','You are a {domain} research expert'),
    ('human','Explain {topic} in simple terms ')
])
prompt=chat_template.invoke({'domain':'cricket' , 'topic': 'LBW'})
print(prompt)