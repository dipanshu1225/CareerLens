import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()


# ==========================================================
# GET GEMINI API KEY
# ==========================================================

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        api_key = None

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing.")


# ==========================================================
# GEMINI CLIENT
# ==========================================================

client = genai.Client(api_key=api_key)


# ==========================================================
# CAREER AI
# ==========================================================

def ask_career_ai(question):

    prompt = f"""
You are CareerLens AI, an AI-powered career assistant.

Your job is to help users with:

- Resume improvement
- Job matching
- Career planning
- Skill gaps
- Interview preparation
- Data Analytics
- Data Science
- Python
- SQL
- Excel
- Power BI
- Machine Learning
- Artificial Intelligence

Give practical, concise and beginner-friendly answers.

User question:
{question}
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        st.error("❌ Gemini API Error")

        st.code(str(e))

        return "I couldn't generate a response right now."