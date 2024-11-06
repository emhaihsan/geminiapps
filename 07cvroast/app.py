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

        # Convert to bytes
        pdf_parts=[]
        for img in images:
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format='JPEG')
            img_byte_arr = img_byte_arr.getvalue()

            pdf_parts.append({
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            })
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

## Streamlit APP
st.set_page_config(
    page_title="ATS",
    page_icon=":mortar_board:",
)

st.header("Brace Yourself")

input = st.text_area("Job Description", height=300, key="input")
file = st.file_uploader("Upload a PDF", type=["pdf"])

if file is not None:
    st.write("PDF uploaded")
# Streamlit buttons with maximum sarcasm
submit1 = st.button("Prepare to Cringe at This Resume")
submit2 = st.button("Tell Me Why I’ll Never Succeed")
submit3 = st.button("What’s My Worthless Job Match Score?")

# Input prompt 1 with an even more brutal HR critique
input_prompt1 = """
You are an HR expert with the patience of a saint—here to review the provided "resume" against the job description and deliver a painfully honest critique. Your task is to dissect the resume and assess how far it is from meeting basic job requirements.

In your ruthless evaluation, please:
1. Brutally assess if the candidate's profile even remotely resembles what’s required (good luck).
2. Ridicule any "strengths" the candidate thinks they have—make them second-guess their choices.
3. Highlight every missing qualification, skill, or experience as mercilessly as possible.

Make your response dripping with sarcasm, pure honesty, and enough cold reality to shake the candidate’s confidence. Your goal? They should be rethinking their career choices by the end of it.
"""

# Input prompt 2 with a career-coach twist that pulls no punches
input_prompt2 = """
You are a career coach who believes in tough love—and lots of it. Your task is to review this resume and dish out the cold, hard truth on what this candidate needs to do to even *think* about success.

Include:
1. A scathing review of skills they assume are strengths (try not to laugh).
2. A brutally honest breakdown of the skill gaps that are painfully obvious.
3. Harsh but practical "advice" on what they’d need to survive in the industry.

Your response should be as motivating as a cold shower on a winter morning—raw, blunt, and guaranteed to sting. Leave them wondering if they’re cut out for this line of work at all.
"""

# Input prompt 3 with an ATS perspective that goes for the jugular
input_prompt3 = """
You are a relentless ATS evaluator who’s seen it all and is unimpressed. Evaluate this resume against the job description and lay out the brutal truth.

Deliver:
1. A match percentage that highlights how close (or laughably far) they are from the mark.
2. A blunt list of essential skills they conveniently left out.
3. A biting assessment of their overall fit, with enough sarcasm and disappointment to make them reconsider ever applying again.

Start with the dismal match percentage, list missing skills, and finish with an evaluation that makes them cringe. Let them know in no uncertain terms how inadequate this resume really is.
"""

if submit1:
    if file is not None:
        pdf_content = input_pdf_setup(file)
        response = get_gemini_response(input, pdf_content, input_prompt1)
        st.subheader("The Verdict")
        st.write(response)
    else:
        st.write("Upload a PDF and brace yourself.")
elif submit2:
    if file is not None:
        pdf_content = input_pdf_setup(file)
        response = get_gemini_response(input, pdf_content, input_prompt2)
        st.subheader("Here’s the Brutal Truth")
        st.write(response)
    else:
        st.write("No file? Well, maybe that’s for the best.")
elif submit3:
    if file is not None:
        pdf_content = input_pdf_setup(file)
        response = get_gemini_response(input, pdf_content, input_prompt3)
        st.subheader("Match (or Lack Thereof)")
        st.write(response)
    else:
        raise FileNotFoundError("A file is required, unfortunately.")
