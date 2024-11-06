"""
YouTube Transcript to Detailed Notes Converter

This application takes in a YouTube video link and extracts the transcript.
Then it uses Google Gemini Pro to generate a detailed summary of the video
within 250 words.
"""

import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

# load all the environment variables from .env file
load_dotenv()

# configure our API key from environment variable
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Prompt template for Google Gemini Pro
prompt = """You are YouTube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words. Please provide the summary of the text given here:  """

# Function to extract transcript details from yt videos
def extract_transcript_details(youtube_video_url):
    """
    This function takes in a YouTube video link and returns the transcript text.
    """
    try:
        # get the video id from the link
        video_id = youtube_video_url.split("=")[1]
        
        # get the transcript text
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        # concatenate the transcript text
        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        # raise an exception if there is an error
        raise e
    
# Function to generate summary based on Prompt from Google Gemini Pro
def generate_gemini_content(transcript_text, prompt):
    """
    This function takes in the transcript text and prompt and returns the
    generated summary text.
    """
    # load the Gemini Pro model
    model = genai.GenerativeModel("gemini-1.5-flash")
    # generate the content
    response = model.generate_content(prompt + transcript_text)
    return response.text

# Streamlit app
st.title("YouTube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    # get the video id from the link
    video_id = youtube_link.split("=")[1]
    # show the thumbnail
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if st.button("Get Detailed Notes"):
    # extract the transcript text
    transcript_text = extract_transcript_details(youtube_link)

    if transcript_text:
        # generate the summary
        summary = generate_gemini_content(transcript_text, prompt)
        # show the summary
        st.markdown("## Detailed Notes:")
        st.write(summary)

