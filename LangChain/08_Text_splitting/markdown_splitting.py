from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter , Language


text="""# Project Name: Smart Student Tracker

A simple Python-based project to manage and track student data, including their grades, age, and academic status.


## Features

- Add new students with relevant info
- View student details
- Check if a student is passing
- Easily extendable class-based design


## 🛠 Tech Stack

- Python 3.10+
- No external dependencies


## Getting Started

1. Clone the repo  
   ```bash
   git clone https://github.com/your-username/student-tracker.git

"""
splitter=RecursiveCharacterTextSplitter.from_language(
    chunk_size=200,
    chunk_overlap=0,
    language=Language.MARKDOWN
)

result=splitter.split_text(text)

print(result[0])