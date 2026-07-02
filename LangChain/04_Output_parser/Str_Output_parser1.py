from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm=HuggingFaceEndpoint(model='meta-llama/Llama-3.1-8B-Instruct',
                        task='text_generation')
model=ChatHuggingFace(llm=llm)

template1=PromptTemplate(template='write a detailed report on {topic}',
                         input_variables=['topic'])

template2=PromptTemplate(template='Write a 5 Line Summary on the following {text}',
                         input_variables=['text'])

parser=StrOutputParser()
                           #(extract string) 
                              #^
                              #|
                              #|
chain = template1 | model | parser | template2 | model | parser # chain pipeline 

result = chain.invoke({'topic': 'Big Bang Theory'})

print(result)
