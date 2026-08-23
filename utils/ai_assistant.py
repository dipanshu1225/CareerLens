import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing. Check your .env file.")

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


def ask_career_ai(question):

    response = client.chat.completions.create(
        model="gemini-3.6-flash",

        messages=[
            {
                "role": "system",
                "content": """
You are CareerLens AI, a professional career assistant.

Help users with:
- Resume improvement
- Job matching
- Career planning
- Skill gaps
- Data Analytics
- Interview preparation
- Python
- SQL
- Power BI

Give practical, concise and professional answers.
Keep responses under 500 words unless the user asks for more detail.
"""
            },
            {
                "role": "user",
                "content": question
            }
        ],

        max_tokens=2000
    )

    return response.choices[0].message.content