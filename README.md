# Gemini LLM Applications

This repository contains a collection of applications built using the Google Generative AI Gemini model. These applications demonstrate various use cases for the Gemini model, including text-to-SQL, conversational chat, document question answering, and image analysis.

## List of Applications

### 1. Gemini Vision Application

An application that uses the Gemini model to analyze images and generate text descriptions.

- **Location**: `01geminillmapp/vision.py`
- **Features**:
  - Upload images (PNG, JPG, JPEG)
  - Image analysis with or without additional prompts
  - Generate detailed descriptions of uploaded images

### 2. Conversational Gemini Chat

A simple chat application that uses the Gemini model to respond to user input.

- **Location**: `02conversationalgemini/qachat.py`
- **Features**:
  - Interactive chat interface
  - Stored chat history
  - Streaming responses

### 3. Invoice Extraction

An application that uses Gemini to extract information from invoices.

- **Location**: `03invoice/app.py`
- **Features**:
  - Invoice image upload
  - Automatic information extraction
  - Invoice detail analysis

### 4. Chat with PDF

An application that allows users to ask questions based on PDF documents.

- **Location**: `04chatwithpdf/app.py`
- **Features**:
  - Multiple PDF upload
  - PDF to text conversion
  - Contextual Q&A

### 5. Document Q&A

An application for answering questions based on a set of documents.

- **Location**: `05documentqa/app.py`
- **Features**:
  - Document vector embedding
  - Similarity search
  - Contextual answers

### 6. Text-to-SQL

An application that converts natural language queries to SQL queries.

- **Location**: `06sqlllm/app.py`
- **Features**:
  - Natural language to SQL conversion
  - Automatic query execution
  - Query results display

### 7. CV Roast

An application for CV evaluation with sharp criticism.

- **Location**: `07cvroast/app.py`
- **Features**:
  - CV analysis against job descriptions
  - Skill development suggestions
  - Match percentage

### 8. ATS (Applicant Tracking System)

An application to evaluate CVs against job requirements.

- **Location**: `08ats/app.py`
- **Features**:
  - CV evaluation
  - Keyword analysis
  - Improvement suggestions

### 9. Food Critics

A food criticism application with a sarcastic style.

- **Location**: `09foodcritics/app.py`
- **Features**:
  - Food image analysis
  - Lifestyle critique
  - Healthy food suggestions

### 10. YouTube Transcript

An application to convert YouTube transcripts into detailed notes.

- **Location**: `10youtubetranscript/app.py`
- **Features**:
  - Transcript extraction
  - Video summarization
  - Thumbnail display

### 11. CrewAI YouTube Blog

An application to create blogs from YouTube content.

- **Location**: `11crewyttoblog/`
- **Features**:
  - Video search
  - Content analysis
  - Automatic blog creation

### 12. CrewAI News

An application to generate news using CrewAI.

- **Location**: `12crewnews/`
- **Features**:
  - News research
  - Article writing
  - Serper API integration

## Requirements

- Google Generative AI API key
- Python 3.9+
- Streamlit
- SQLite

## Notes

- Ensure all API keys are properly configured
- Some applications may require additional setup (like databases)
- Detailed documentation available in each application folder
