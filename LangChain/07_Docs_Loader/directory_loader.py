from langchain_community.document_loaders import PyPDFLoader , DirectoryLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint

load_dotenv()

loader=DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs=loader.load()
# docs=loader.lazy_load()  #for large numbers of data / PDF

print(len(docs))