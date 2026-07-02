from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm=HuggingFaceEndpoint(model='meta-llama/Llama-3.1-8B-Instruct',
                        task='text_generation')
model=ChatHuggingFace(llm=llm)

template1=PromptTemplate(template='write a detailed report on {topic}',
                         input_variables=['topic'])

template2=PromptTemplate(template='Write a 5 Line Summary on the following {text}',
                         input_variables=['text'])

prompt1=template1.invoke({'topic': 'Black hole'})

result=model.invoke(prompt1)

prompt2=template2.invoke({'text': result.content})

result2=model.invoke(prompt2)

print(result2.content)
