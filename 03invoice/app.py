import os
from PIL import Image
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv() ## load all the environment variables from .env file

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load Gemini Pro model and get responses

model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt]) # generate response from input
    return response.text

def input_image_details(file):
    if file is not None:
        bytes_data = file.getvalue()

        image_parts = [
            {
                "mime_type": file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# initialize our streamlit app

st.set_page_config(
    page_title="Invoice Extractor")

st.header("Invoice Extractor")

input = st.text_input("Input: ", key="input")

file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
image = ""
if file is not None:
    image = Image.open(file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Tell me about the Invoice")

input_prompt = """
You are an expert in understanding invoices. We will upload an image and extract the invoice. and you will have to answer any questions based on the uploaded invoice image
"""

# if submit is clicked
if submit:
    image_data = input_image_details(file)
    response=get_gemini_response(input, image_data, input_prompt)
    st.subheader("The Response is")
    st.write(response)