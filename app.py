import numpy as np
import streamlit as st
import pandas as pd
from utils.ai_assistant import ask_career_ai

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
#HOME
st.set_page_config(
    page_title="CareerLens",
    page_icon="🤖",
    layout="wide"
)
#
#Header

st.title("CareerLens")

st.subheader("AI-Powered Resume & Career Intelligence")

st.write(
    "Analyze your resume. Match it with jobs."
)

st.write(
    "Discover your skill gaps. Improve your chances."
)

st.divider()

#Metric cards
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "📄Resume Score",
    "82%",
    border=True
)

col2.metric(
    "🧠Skill Found",
    "18",
    border=True
)

col3.metric(
    "🎯Jobs Matched",
    "7",
    border=True
)

col4.metric(
    "📈Skill Matched",
    "68%+",
    border=True
)

#Quick actions
st.subheader("🚀What do you want to do?")

col1,col2,col3 = st.columns(3)
with col1:
    if st.button("📄 Analyze Resume", use_container_width=True):
        st.switch_page("pages/resume_analyzer.py")

with col2:
    if st.button("🎯 Match With Job", use_container_width=True):
        st.switch_page("pages/job_matcher.py")

with col3:
    if st.button("📊 Find Skill Gaps", use_container_width=True):
        st.switch_page("pages/skill_gap.py")
st.divider()

# ==================================================
# CareerLens AI Assistant
# ==================================================

st.header("🤖 CareerLens AI Assistant")

st.write(
    "Your personal AI career & resume assistant"
)


with st.container(border=True):


    st.write(
        "👋 Hi! I'm CareerLens AI."
    )

    st.write(
        "I can help you improve your resume, "
        "understand job requirements, find skill gaps, "
        "prepare for interviews, and plan your career."
    )


    user_question = st.chat_input(
        "Ask CareerLens anything about your career..."
    )

    if user_question:

        # User message
        with st.chat_message("user"):
            st.write(user_question)

        # AI response
        with st.chat_message("assistant"):

            with st.spinner("🤖 CareerLens is thinking..."):

                answer = ask_career_ai(user_question)

            st.write(answer)
            
st.divider()