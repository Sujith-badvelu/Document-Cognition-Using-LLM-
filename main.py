import os
from groq import Groq

os.environ["GROQ_API_KEY"] = "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"
client = Groq()
response = client.chat.completions.create(
    messages = [
        {"role": "user", "content": "what is multiples  of 10"}
    ],
    # "llama-3.1-8b-instant" 
    model = "llama3-70b-8192"
)    
langchain= response
output = response.choices[0].message.content  
print(output)   




# document cognition

# import streamlit as st
# import os
# from langchain_groq import ChatGroq
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.chains.combine_documents import create_stuff_documents_chain
# from langchain_core.prompts import ChatPromptTemplate
# from langchain.chains import create_retrieval_chain
# from langchain_community.vectorstores import FAISS  
# # Faiss is a library for efficient similarity search and clustering of dense vectors.
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from dotenv import load_dotenv
# from PyPDF2 import PdfReader
# load_dotenv()   
# ## load the GROQ and GOOGLE
 
# groq_api_key="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"
# google_api_key= "AIzaSyBxp6aTOPlptgKqNiZVFHxs0yY4kXDHR1g"

# st.title("Chatgroq With Llama 3.1")
# llm=ChatGroq(groq_api_key=groq_api_key,model_name="llama-3.1-8b-instant",temperature=0)
# prompt=ChatPromptTemplate.from_template(
# """
# Answer the questions based on the provided context only.
# Please provide the most accurate response based on the question
# from the databse that you have only dont try to make assumption
# on your own 
# <context>
# {context}
# <context>
# Questions:{input}

# """
# )
# def load_pdf(pdf_docs):
#     text=""
#     for pdf in pdf_docs:
#         pdf_reader=PdfReader(pdf)
#         for page in pdf_reader.pages:
#             text+=page.extract_text()
#     return text

# def get_text_chunks(text):
#     text_splitter=RecursiveCharacterTextSplitter(
#         chunk_size=100,chunk_overlap=0
#     )
#     chunks = text_splitter.split_text(text)
#     return chunks

# def vector_embedding():
#     try:
#         embeddings=GoogleGenerativeAIEmbeddings(google_api_key=google_api_key,model="models/embedding-001")
#         docs=load_pdf(pdf_docs)
#         cleaned_text=get_text_chunks(docs)
#         vectors = FAISS.from_texts(cleaned_text, embeddings)
#         vectors.save_local("faiss_index2")
#     except:
#          st.error("Try Again")

# # Button to trigger document embedding
# pdf_docs = st.sidebar.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
# if st.sidebar.button("Documents Embedding"):
#     vectors = vector_embedding()  # Store the output in session state
#     st.sidebar.success("Vector Store DB Is Ready")

# # Input for the user question
# prompt1 = st.text_input("Enter Your Question From Documents")

# #If the button is clicked
# if prompt1:
#     try:
#         document_chain = create_stuff_documents_chain(llm,prompt)
#         #Load the vectorstore from the local directory
#         embeddings=GoogleGenerativeAIEmbeddings(google_api_key=google_api_key,model="models/embedding-001")
#         new_vectors = FAISS.load_local("faiss_index2", embeddings,allow_dangerous_deserialization=True)
#         retriever = new_vectors.as_retriever()
#         retrieval_chain = create_retrieval_chain(retriever,document_chain)    
#         response = retrieval_chain.invoke({'input': prompt1})
#         st.write(response['answer'])
#     except Exception as e:
#                     st.error(f"Error vector not Found : please click the Documents embeddings first {e} ")  
