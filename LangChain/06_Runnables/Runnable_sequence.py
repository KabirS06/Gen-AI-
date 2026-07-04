from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm=HuggingFaceEndpoint(model='meta-llama/Llama-3.1-8B-Instruct',
                        task='text_generation')
model=ChatHuggingFace(llm=llm)

prompt1=PromptTemplate(template='Write a joke about {topic}',
                      input_variables=['topic'])

parser=StrOutputParser()

prompt2=PromptTemplate(template='Explain the joke : {joke}',
                       input_variables=['joke'])

chain=RunnableSequence(prompt1 , model , parser , prompt2 ,model ,parser)

print(chain.invoke({'topic': 'Black people'}))