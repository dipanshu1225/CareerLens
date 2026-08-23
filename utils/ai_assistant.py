import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Get API key from local .env or Streamlit Cloud Secrets
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        api_key = None

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing.")

# Gemini client
client = genai.Client(api_key=api_key)


def ask_career_ai(question):

    prompt = f"""
You are CareerLens AI, a helpful career assistant.

Help the user with:
- Resume improvement
- Job searching
- Career planning
- Skill development
- Interview preparation
- Job descriptions
- Data Science
- Data Analytics
- Python
- AI and Machine Learning

Give practical, clear and beginner-friendly answers.

User question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text