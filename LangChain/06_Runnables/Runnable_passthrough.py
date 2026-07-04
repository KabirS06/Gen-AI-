from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel ,RunnableSequence , RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(model='meta-llama/Llama-3.1-8B-Instruct',
                        task='text_generation')
model=ChatHuggingFace(llm=llm)


prompt1=PromptTemplate(template='Write a joke about {topic}',
                      input_variables=['topic'])

parser=StrOutputParser()

prompt2=PromptTemplate(template='Explain the joke : {joke}',
                       input_variables=['joke'])

joke_gen_chain=RunnableSequence(prompt1 ,model,parser)

parallel_chain=RunnableParallel({
    'joke' : RunnablePassthrough(),
    'explanation' : RunnableSequence(prompt2 , model , parser)
})
final_chain=RunnableSequence(joke_gen_chain , parallel_chain)
result =final_chain.invoke({'topic':'Cricket'})

print(result)
print("\n ------------JOKE---------\n")
print(result['joke'])
print("\n ------------EXPLANATION---------\n")
print(result['explanation'])