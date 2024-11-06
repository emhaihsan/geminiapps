"""
ATS Application

This application takes in a job description and a PDF resume.
It converts the PDF to an image and then uses Google Gemini Pro
to generate a response based on the job description and the resume.

The application has three modes:
1. Detailed evaluation of the resume against the job description.
2. Practical advice on how the candidate can improve their skills.
3. Match percentage indicating how well the resume aligns with the job description.

The application uses the following functions:
- get_gemini_response: takes in the job description, the resume (as an image), and a prompt, and returns the response from Google Gemini Pro.
- input_pdf_setup: takes in a PDF file and converts it to an image.
"""

import os
import pdf2image
from PIL import Image
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import io
import base64

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content, prompt):
    """
    Takes in a job description, the resume (as an image), and a prompt,
    and returns the response from Google Gemini Pro.
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input, pdf_content[0], prompt]) # generate response from input
    return response.text

def input_pdf_setup(uploaded_file):
    """
    Takes in a PDF file and converts it to an image.
    """
    if uploaded_file is not None:
        # Convert the PDF to image
        images=pdf2image.convert_from_bytes(uploaded_file.read())

        first_page=images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

## Streamlit APP
st.set_page_config(
    page_title="ATS",
    page_icon=":mortar_board:",
)

st.header("ATS Application")

input = st.text_area("Job Description", height=300, key="input")
file = st.file_uploader("Upload a PDF", type=["pdf"])

if file is not None:
    st.write("PDF uploaded")

submit1 = st.button("Tell me about the resume")

submit2 = st.button("How Can I Improvise my Skills")

submit3 = st.button("Percentage Matching")

input_prompt1 = """
You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description and provide a detailed evaluation. 

In your assessment, please:
1. Clearly state whether the candidate's profile aligns with the job requirements.
2. Highlight specific strengths that make the candidate a good fit.
3. Identify any weaknesses or missing qualifications in relation to the job requirements.

Your evaluation should be professional, concise, and focused on the candidate’s suitability for this role.
"""

input_prompt2 = """
You are an experienced career coach and skill development expert. Your task is to review the provided resume and provide practical advice on how the candidate can improve their skills to better align with industry demands.

Please focus on the following in your response:
1. Highlight key skills the candidate has that are valuable for their career path.
2. Identify any skill gaps or areas where improvement is needed.
3. Suggest specific steps, courses, or resources the candidate can pursue to enhance their qualifications.

The response should be actionable, encouraging, and tailored to help the candidate grow in their career.
"""

input_prompt3 = """
You are a skilled Applicant Tracking System (ATS) evaluator with expertise in data science and ATS functionality. Your task is to evaluate the resume against the provided job description.

Provide the following in your response:
1. A match percentage indicating how well the resume aligns with the job description.
2. A list of missing keywords or skills that are critical for the role.
3. Final thoughts on the candidate's overall fit for the position, including any areas of improvement.

This output should be structured with the match percentage first, followed by missing keywords, and ending with your overall assessment.
"""

if submit1:
    if file is not None:
        pdf_content = input_pdf_setup(file)
        response = get_gemini_response(input, pdf_content, input_prompt1)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload a PDF file")
elif submit2:
    if file is not None:
        pdf_content = input_pdf_setup(file)
        response = get_gemini_response(input, pdf_content, input_prompt2)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload a PDF file")
elif submit3:
    if file is not None:
        pdf_content = input_pdf_setup(file)
        response = get_gemini_response(input, pdf_content, input_prompt3)
        st.subheader("The Response is")
        st.write(response)
    else:
        raise FileNotFoundError("No file uploaded")

