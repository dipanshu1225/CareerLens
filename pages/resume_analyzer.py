import streamlit as st
from pypdf import PdfReader
from utils.parser import extract_text_from_pdf, detect_skills 

#for style css
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#Page configuration    
st.set_page_config(
    page_title = "RESUME ANALYZER | CareerLens AI",
    page_icon= "📄",
    layout = "wide"
)
# Back to Dashboard
if st.button("← Back to Dashboard"):
    st.switch_page("app.py")
    

st.title("📄 Resume Analyzer")
st.write("Upload your resume and let CareerLens AI analyze your skills and profile.")
st.divider()

# Default values
# -------------------------------

found_skills = []
resume_text = ""
score = 0
experience = "Fresher"

#RESUME UPLOAD
#----------------------------------------------------------
uploaded_file = st.file_uploader("Upload Your Resume",
                                type= ["pdf"],
                                help = "Upload Your Resume in Pdf format.")

if uploaded_file:
    st.success(f"{uploaded_file.name}✅Uploaded Successfully!")
 
    # Extract text
    resume_text = extract_text_from_pdf(uploaded_file)

    # Detect skills
    found_skills = detect_skills(resume_text)
    

    st.divider()   
#================================================================
###METRIC CARDS###

col1, col2,col3 = st.columns(3)
if uploaded_file:

    resume_text = extract_text_from_pdf(uploaded_file)

    found_skills = detect_skills(resume_text)

    # Calculate score HERE
    score = 0

    if resume_text:
        score += 20

    if found_skills:
        score += 20

    if len(found_skills) >= 5:
        score += 10

    if len(resume_text) >= 1000:
        score += 10

    if "experience" in resume_text.lower():
        score += 10

    if "project" in resume_text.lower():
        score += 10

    if "education" in resume_text.lower():
        score += 10

    if "github" in resume_text.lower() or "linkedin" in resume_text.lower():
        score += 10

    score = min(score, 100)

col1.metric("📊 Resume Score", f"{score}%",border =True)
col2.metric("🧠 Skills Found", len(found_skills),border =True)
col3.metric("💼 Experience", "Fresher",border =True)

#Resume Insights
st.subheader("🔍 Resume Insights")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### ✅ Detected Skills")

    if found_skills:
    
        for skill in found_skills:
                st.write(f"• {skill}")
    
    else:
        st.warning("No known skills detected.")
    

if uploaded_file:
    with col2:
        st.markdown("### ⚠️ Areas to Improve")

        improvements = [
            "Add more measurable achievements",
            "Improve project descriptions",
            "Add relevant keywords",
            "Include GitHub/portfolio links"
        ]

        for item in improvements:
            st.write(f"• {item}")
        
        
## REsume score portion

st.subheader("📈 Resume Evaluation")

st.progress(score/100)

if score>=80:
    st.success("Excellent resume! Your profile is strong.")
elif score >= 60:
    st.warning("Good resume, but there is room for improvement.")
else:
    st.error("Your resume needs significant improvement.")
    
    
###View Extracted section
with st.expander("📄 View Extracted Resume Text"):

    st.text_area(
        "Resume Content",
        resume_text,
        height=300
    )    