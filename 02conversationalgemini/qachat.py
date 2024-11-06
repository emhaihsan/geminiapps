import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")
chat=model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True) # generate response from input
    return response

st.set_page_config(
    page_title="Q&A demo using Google Generative AI",
)

st.header("Gemini Chat Application")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input: ", key="input")

submit = st.button("Submit")

if submit and input:
    response = get_gemini_response(input)
    ## Add user query and response to session chat history
    st.session_state['chat_history'].append(("User", input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Gemini", chunk.text))

st.subheader("Chat History")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}") 