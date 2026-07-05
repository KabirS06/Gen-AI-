from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader('../07_Docs_Loader/dl-curriculum.pdf')

docs=loader.load()

splitter=RecursiveCharacterTextSplitter(
    chunk_size=249,
    chunk_overlap=0
)

chunks=splitter.split_documents(docs)

print(chunks[0].page_content)

# always preffered over character based text splitter
