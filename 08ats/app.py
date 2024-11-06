import os
import PyPDF2 as pdf
import streamlit as st
from dotenv import load_dotenv 
import google.generativeai as genai

load_dotenv() ## load all the environment variables from .env file

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Gemini Pro Response
def get_gemini_response(input):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(input) # generate response from input
    return response.text

def input_pdf_text(uploaded_file):
    """
    Takes in a PDF file and converts it to text.
    """
    pdf_reader = pdf.PdfFileReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extractText()
    return text

# Prompt Template

input_prompt = """
Listen up. You’re going to act as the world’s most "elite" ATS evaluator—a relentless, all-knowing machine with a sixth sense for spotting disastrous resumes in the ultra-competitive tech field. Your areas of “expertise” span software engineering, data science, data analysis, and big data engineering. You’re here to review the resume against the job description (JD), and believe me, you’ve seen some shockers in your time.

Here’s the deal:
1. **Match Percentage**: Assign a JD match percentage to expose just how “aligned” (or painfully misaligned) this resume is with reality.
2. **Missing Keywords**: Ruthlessly list any essential skills or keywords the candidate "somehow forgot" that they need for even a slim chance of making it past the first round.
3. **Profile Summary**: Round it off with a scathing summary of your findings, keeping it brief but brutal.

Remember, we’re in a cutthroat job market—so be as direct as possible. No sugar-coating. Let’s give this candidate the "reality check" they didn’t know they needed.

resume: {text}
description: {jd}

The response should be a single string with this structure:
{{"JD Match": "XX%", "MissingKeywords": ["Keyword1", "Keyword2"], "Profile Summary": "Insert painfully honest, reality-shattering summary here"}}
"""


## streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_response(input_prompt)
        st.subheader(response)