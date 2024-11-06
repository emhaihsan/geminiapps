import os
import streamlit as st
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv() # load environment variables from .env.

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")


def get_conversational_chain():
    prompt_template = """
    Answer the question as truthfully as possible using the context below, make sure to provided context just enough to answer the question.
    if you don't know the answer, just say that you don't know, don't try to make up an answer.
    Context:\n{context}?\n
    Question:\n{question}\n

    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)

    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)
    chain = get_conversational_chain()

    response =  chain({"input_documents": docs, "question": user_question})
    print(response)
    st.write("Reply: ", response["output_text"])

def main():
    st.set_page_config(page_title="Chat with PDF", page_icon=":books:")
    st.header("Chat with PDF :books:")

    user_question = st.text_input("Ask a question about your PDF: ", key="input")
    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Upload your PDF")
        pdf_docs = st.file_uploader("Upload your PDF", type="pdf", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                # get the text of pdf
                raw_text = get_pdf_text(pdf_docs)
                # get the text chunks
                text_chunks = get_text_chunks(raw_text)
                # get the vector store
                get_vector_store(text_chunks)
                st.success("Done")


if __name__ == "__main__":
    main()