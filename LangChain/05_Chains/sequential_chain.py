from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm=HuggingFaceEndpoint(model='meta-llama/Llama-3.1-8B-Instruct',
                        task='text_generation')
model=ChatHuggingFace(llm=llm)

prompt1=PromptTemplate(
    template='give a detailed report on {topic}',
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template='Generate the Summary on the following report in 10 lines : {text}',
    input_variables=['text']
)

parser=StrOutputParser()

chain=prompt1 | model | parser | prompt2 | model |parser

result=chain.invoke({'topic':'Black Hole'})

print(result)