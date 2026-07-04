from langchain_community.document_loaders import PyPDFLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint

load_dotenv()

loader=PyPDFLoader('dl-curriculum.pdf')
docs=loader.load()

print(docs[0].page_content)
print("\n ---------------------------------------------------\n")
print(docs[0].metadata)