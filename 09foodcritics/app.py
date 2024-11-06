import os
from PIL import Image
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, image):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input, image[0]]) # generate response from input
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
    

# Initialize the Streamlit app
st.set_page_config(page_title="Gemini Lifestyle Critic")

st.header("Gemini Lifestyle Critic")
uploaded_file = st.file_uploader("Upload an image of your meal...if you dare.", type=["jpg", "jpeg", "png"])
image = ""   

# Display the uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Your 'Meal' Upload", use_column_width=True)

# Button to submit for critique
submit = st.button("Unleash the Critique")

# Prompt untuk menghasilkan kritik pedas dan kasar terhadap makanan
input_prompt = """
Lo adalah kritikus gaya hidup dan nutrisi yang nggak punya toleransi untuk pilihan makanan yang buruk. 
Analisa gambar makanan yang diunggah, dan kasih komentar sepedas mungkin tentang pilihan gaya hidup yang ini.

1. Kalau ada yang sehat, bolehlah kasih apresiasi dikit, tapi jangan berlebihan.
2. Kalau makanannya nggak sehat, kritik sekeras mungkin. Pakai sarkasme, sindiran tajam, dan humor gelap.
   Bikin mereka mikir ulang buat makan beginian lagi. Jangan sungkan-sungkan, kritik lo harus cukup tajam
   buat bikin mereka nyesel dan malu.

Format output:
- Evaluasi sinis dan penuh sarkas yang ngasih tahu ini makanan buat manusia apa bukan.
- Kasih daftar makanan yang sehat dan beri apresiasi, tapi secukupnya aja, jangan bikin mereka ge-er.
- List makanan yang jauh dari sehat, dan kasih kritik yang bikin mereka nyesel makan ini.

Bikin pengguna ngerasa lo kecewa berat sama pilihan hidup mereka.
"""

# If the submit button is clicked
if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data)
    st.subheader("Gemini's Brutal Verdict")
    st.write(response)
