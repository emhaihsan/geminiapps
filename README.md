# Gemini LLM Applications

This repository contains a collection of applications built using the Google Generative AI Gemini model. The applications demonstrate various use cases for the Gemini model, including text-to-SQL, conversational chat, document question answering, and image analysis.

## Applications

### 1. Conversational Gemini Chat

A simple chat application that uses the Gemini model to respond to user input.

- Code: `02conversationalgemini/qachat.py`
- Description: This application demonstrates how to use the Gemini model to generate human-like responses to user input.

### 2. Text-to-SQL

An application that uses the Gemini model to convert natural language queries into SQL queries.

- Code: `06sqlllm/app.py`
- Description: This application demonstrates how to use the Gemini model to generate SQL queries from natural language input.

### 3. Document Question Answering

An application that uses the Gemini model to answer questions based on a set of documents.

- Code: `05documentqa/app.py`
- Description: This application demonstrates how to use the Gemini model to answer questions based on a set of documents.

### 4. Image Analysis

An application that uses the Gemini model to analyze images and generate text descriptions.

- Code: `01geminillmapp/vision.py`
- Description: This application demonstrates how to use the Gemini model to generate text descriptions of images.

### 5. Invoice Extractor

An application that uses the Gemini model to extract information from invoices.

- Code: `03invoice/app.py`
- Description: This application demonstrates how to use the Gemini model to extract information from invoices.

### 6. Chat with PDF

An application that uses the Gemini model to answer questions based on a PDF document.

- Code: `04chatwithpdf/app.py`
- Description: This application demonstrates how to use the Gemini model to answer questions based on a PDF document.

## Requirements

- Google Generative AI API key
- Python 3.9+
- Streamlit
- SQLite

## Setup

1. Set up a Google Generative AI API key and add it to your environment variables
2. Run the application using `streamlit run app.py`
