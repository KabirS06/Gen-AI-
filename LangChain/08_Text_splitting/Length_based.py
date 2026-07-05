from langchain_classic.text_splitter import CharacterTextSplitter
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader('Gen-AI-/LangChain/07_Docs_Loader/dl-curriculum.pdf')

docs=loader.lazy_load()

spliiter=CharacterTextSplitter(chunk_size=150, chunk_overlap=0 , separator='')

result=spliiter.split_documents(docs)

print(result[0].page_content)
