from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm=HuggingFaceEndpoint(model='meta-llama/Llama-3.1-8B-Instruct',
                        task='text_generation')
model=ChatHuggingFace(llm=llm)

parser=StrOutputParser()

prompt=PromptTemplate(
    template="Give me  5 interesting facts about {topic}",
    input_variables=['topic'])

chains=  prompt | model | parser

result=chains.invoke({'topic':'Black hole'})

print(result)
