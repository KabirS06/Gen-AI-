from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel ,RunnableSequence
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(model='meta-llama/Llama-3.1-8B-Instruct',
                        task='text_generation')
model=ChatHuggingFace(llm=llm)

prompt1=PromptTemplate(template='Generate a tweet about {topic}',
                      input_variables=['topic'])

prompt2=PromptTemplate(template='Generate a LinkedIn post about {topic}',
                       input_variables=['topic'])
parser=StrOutputParser()

parralel_chain=RunnableParallel({
    'tweet':RunnableSequence(prompt1 , model ,parser ),
    'LinkedIn': RunnableSequence(prompt2 , model , parser),
})

result=parralel_chain.invoke({'topic':'Internship'})

print(result['tweet'])
print(result['LinkedIn'])