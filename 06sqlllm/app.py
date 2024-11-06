# Agenda - Text to SQL LLM Application
"""
Prompt --> LLM --> Gemini --> Query --> SQL --> Response

Implementation:
1. SQLITE -- insert-- python
2. LLM -- Gemini -- SQL
"""

from dotenv import load_dotenv
load_dotenv() ## load all the environment variables from .env file

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

## configure our API key from environment variable

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load google gemini model and provide query as response

def get_gemini_response(question, prompt):
    """
    This function takes in a question and a prompt, 
    uses the Gemini model to generate an SQL query, 
    and returns the result of the query
    """
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([prompt[0], question]) # generate response from input
    print(response.text)
    sql_query = response.text.strip().replace("```", "")  # Remove any backticks or extra formatting
    sql_query = sql_query.replace("sql", "")  # Remove any backticks or extra formatting
    return sql_query

## function to retrieve query from the sql database

# def read_sql_query(sql, db):
#     """
#     This function takes in a SQL query and a database, 
#     and returns the result of the query
#     """
#     conn = sqlite3.connect(db)
#     cursor = conn.cursor()
#     cursor.execute(sql)
#     rows = cursor.fetchall()
#     conn.commit()
#     conn.close()
#     return rows

def read_sql_query(sql,db):
    print(sql)
    print(db)
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    rows=cur.execute(sql).fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

prompt=[
"""
You are an expert in converting English questions into precise, executable SQL queries.

The SQL database is named STUDENT and has the following columns:
- NAME
- CLASS
- SECTION
- MARKS

Guidelines:
1. Generate SQL queries that directly answer the question.
2. Do NOT include any formatting, backticks (``````), or extraneous text (such as "sql").
3. Ensure the SQL output is a simple, executable command without any additional characters.

Examples:

- Input: "How many entries of records are present?"
  Output: SELECT COUNT(*) FROM STUDENT;

- Input: "Tell me all the students studying in Data Science class."
  Output: SELECT * FROM STUDENT WHERE CLASS = 'Data Science';

Important:
- Return only the SQL code as plain text. No backticks, code blocks, or additional notes.
- If uncertain, use basic SQL syntax that can execute directly in SQLite.
"""

]

## Streamlit App

st.set_page_config(page_title="I can Retrieve any SQL query")
st.header("Gemini App to Retrieve SQL Data")

question = st.text_input("Input: ", key="input")
submit = st.button("Submit")

# if submit clicked
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    data = read_sql_query(response, "student.db")
    print(data)
    st.subheader("The Response is")
    for row in data:
        print(row)
        st.header(row)