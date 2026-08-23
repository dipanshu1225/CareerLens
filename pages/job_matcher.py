import streamlit as st
from utils.parser import( extract_text_from_pdf,detect_skills)

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
    page_title = "Job matcher",
    page_icon="🎯",
    layout= "wide"
)

# ROLE SKILLS
# ==========================================================

ROLE_SKILLS = {
    "Data Analyst": [
        "Python",
        "SQL",
        "Excel",
        "Power BI",
        "Pandas",
        "NumPy",
        "Matplotlib",
        "Statistics",
        "Tableau",
        "Data Visualization"
    ],

    "Data Scientist": [
        "Python",
        "SQL",
        "Pandas",
        "NumPy",
        "Scikit-learn",
        "Machine Learning",
        "Statistics",
        "Matplotlib",
        "Seaborn",
        "TensorFlow"
    ],

    "Machine Learning Engineer": [
        "Python",
        "Machine Learning",
        "Scikit-learn",
        "TensorFlow",
        "PyTorch",
        "NumPy",
        "Pandas",
        "SQL",
        "Git",
        "Docker"
    ],

    "Python Developer": [
        "Python",
        "OOP",
        "Flask",
        "Django",
        "REST API",
        "SQL",
        "Git",
        "GitHub"
    ],

    "AI/ML Engineer": [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "PyTorch",
        "NumPy",
        "Pandas",
        "Scikit-learn",
        "SQL"
    ],

    "Business Analyst": [
        "Excel",
        "SQL",
        "Power BI",
        "Tableau",
        "Statistics",
        "Data Analysis",
        "Communication"
    ],

    "Software Developer": [
        "Python",
        "Java",
        "C++",
        "SQL",
        "OOP",
        "Git",
        "GitHub",
        "Data Structures",
        "Algorithms"
    ]
}

# Back to Dashboard
if st.button("← Back to Dashboard"):
    st.switch_page("app.py")
    
#Header
st.title("🎯 Job Matcher")

st.write(
    "Compare your resume with a target job and discover "
    "how well your skills match the requirements."
)

st.divider()

#Input Section
#-------------------------------------------
st.subheader("📋 Job Matching")

col1, col2 = st.columns(2)

with col1:
    st.markdown("Upload Resume")
    
    uploaded_file = st.file_uploader("Chose your Resume",type=["pdf"],key="job_resume")
    
with col2:
        st.markdown("### 💼 Target Job Role")

        job_role = st.selectbox(
            "Select your target role",
            list(ROLE_SKILLS.keys())
        )
        
st.markdown("### 📝 Paste Job Description")

job_description = st.text_area(
    "Job Description",
    placeholder="""We are looking for a Data Analyst with strong SQL,
Python, Excel and Power BI skills...""",
    height=220
)


st.write("")

analyze_button= st.button("🚀 Analyze Match",
                          use_container_width=True,
                          type = "primary"
                          )

#Analyze Match

if analyze_button:
    if uploaded_file is None:
        st.error("⚠️ Please upload your resume first.")
    else:
        resume_text = extract_text_from_pdf(uploaded_file)
        
        resume_skills = detect_skills(resume_text)
        
        # Detect skills from job description
        # Get required skills for selected job role
        job_skills = ROLE_SKILLS[job_role]

        # Convert to lowercase sets
        resume_skill_set = {
            skill.lower() for skill in resume_skills
        }

        job_skill_set = {
            skill.lower() for skill in job_skills
        }

        # Matching skills
        matched_skills = [
            skill for skill in job_skills
            if skill.lower() in resume_skill_set
        ]

        # Missing skills
        missing_skills = [
            skill for skill in job_skills
            if skill.lower() not in resume_skill_set
        ]

        # Calculate match score
        if len(job_skill_set) > 0:

            match_score = round((len(matched_skills) / len(job_skill_set)) * 100)

        else:

            match_score = 0

        
#Match Result
        st.divider()

        st.subheader("📊 Resume Match Score")

        score_col1, score_col2, score_col3 = st.columns(3)

        with score_col1:

            st.metric(
                "🎯 Match Score",
                f"{match_score}%",
                border=True
            )

        with score_col2:

            st.metric(
                "✅ Skills Matched",
                len(matched_skills),
                border=True
            )

        with score_col3:

            st.metric(
                "❌ Skills Missing",
                len(missing_skills),
                border=True
            )

#Match status
        if match_score >= 80:
            st.success("🟢 Strong Match")

        elif match_score >= 60:
            st.warning("🟡 Moderate Match")

        else:
            st.error("🔴 Weak Match!")

        st.progress(match_score / 100)
            
#Skills Comparison
        st.subheader("🔍 Skill Comparison")

        skills_col1, skills_col2 = st.columns(2)


        # Matched skills
        with skills_col1:

            st.markdown("### ✅ Skills Found")

            if matched_skills:

                for skill in matched_skills:
                    st.write(f"✅ **{skill}**")

            else:

                st.info(
                    "No matching skills were found."
                )


        # Missing skills
        with skills_col2:

            st.markdown("### ❌ Missing Skills")

            if missing_skills:

                for skill in missing_skills:
                    st.write(f"❌ **{skill}**")

            else:

                st.success(
                    "🎉 You have all detected job skills!"
                )
                
# Resume Skills
        

        st.divider()

        st.subheader("🧠 Skills Detected in Your Resume")

        if resume_skills:

            skill_text = " • ".join(resume_skills)

            st.info(skill_text)

        else:

            st.warning(
                "No known skills were detected in your resume."
            )

