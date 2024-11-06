import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv() # load environment variables from .env.

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load Gemini Pro model and get responses

model = genai.GenerativeModel()

def get_gemini_response(question):
    response = model.generate_content(question) # generate response from input
    return response.text

## initialize our streamlit app

st.set_page_config(
    page_title="Q&A demo using Google Generative AI",)

st.header("Gemini LLM Application")

input = st.text_input("Input: ", key="input")
submit = st.button("Submit")

## When submit is clicked

if submit:
    response = get_gemini_response(input)
    st.write(response)

