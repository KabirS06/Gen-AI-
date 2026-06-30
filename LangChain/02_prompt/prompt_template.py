from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate , load_prompt

load_dotenv()

llm=HuggingFaceEndpoint(model='meta-llama/Llama-3.1-8B-Instruct',
                          task='text_generation')
model=ChatHuggingFace(llm=llm)

st.header("Research Tool")

# Dynamic Prompting
paper_input=st.selectbox("Select Research Paper Name", ["Attention Is All You Need",
                                                        "BERT: Pre-training of Deep Bidirectional Transformers",
                                                        "GPT-3: Language Models are Few-Shot Learners",
                                                        "Diffusion Models Beat GANs on Image Synthesis"])
style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )


#loads template
template=PromptTemplate(template="""Please summarize the research paper titled \"{paper_input}\" with the following specifications:\nExplanation Style: {style_input} 
                         \nExplanation Length: {length_input}  \n1.
                         Mathematical Details:  \n   - Include relevant mathematical equations if present in the paper. 
                         \n   - Explain the mathematical concepts using simple, intuitive code snippets where applicable. 
                         \n2. Analogies:  \n   - Use relatable analogies to simplify complex ideas. 
                         \nIf certain information is not available in the paper, respond with: \"Insufficient information available\" instead of guessing.  
                        \nEnsure the summary is clear, accurate, and aligned with the provided style and length.\n""",
                        input_variables=['paper_input','style_input', 'length_input'])
#storing template in a variable
prompt=template.invoke({'paper_input': paper_input , 'style_input': style_input , 'length_input': length_input})

if st.button("Summarize"):
    result=model.invoke(prompt)
    st.write(result.content)

