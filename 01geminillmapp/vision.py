import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

load_dotenv() # load environment variables from .env.

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load Gemini Pro model and get responses

model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input, image):
    if input !="":
        response = model.generate_content([input, image]) # generate response from input
    else:
        response = model.generate_content(image)
    return response.text


st.set_page_config(
    page_title="Q&A demo using Google Generative AI",
)

st.header("Gemini Vision Application")

input = st.text_input("Input: ", key="input")

file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
image = ""

if file is not None:
    image = Image.open(file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Tell me about the image")

# if submit is clicked
if submit:
    response = get_gemini_response(input, image)
    st.write(response)