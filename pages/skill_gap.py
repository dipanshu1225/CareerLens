import streamlit as st
from utils.parser import (extract_text_from_pdf,detect_skills)

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
    page_title="Skill Gap Analyzer",
    page_icon="📊",
    layout="wide"
)


# Back to Dashboard
if st.button("← Back to Dashboard"):
    st.switch_page("app.py")
# -----------------------------------------
# Header
# -----------------------------------------

st.title("📊 Skill Gap Analyzer")

st.write(
    "Discover the skills you need to develop "
    "for your target career."
)

st.divider()

#Input
st.subheader("🎯 Career Target")
col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader(
        "📄 Upload Your Resume",
        type=["pdf"],
        key="skill_gap_resume"
    )


with col2:

    target_role = st.selectbox(
        "💼 Select Target Role",
        [
            "Data Analyst",
            "Data Scientist",
            "Machine Learning Engineer",
            "Python Developer",
            "AI/ML Engineer",
            "Business Analyst"
        ]
        
    )

st.write("")

analyze_button = st.button(
    "🔎 Analyze Skill Gap",
    use_container_width=True,
    type="primary"
)

#Analyze 
if analyze_button:
    if uploaded_file is None:
        st.error("⚠️ Please upload your resume.")
    else:
        resume_text = extract_text_from_pdf(uploaded_file)
        resume_skills = detect_skills(resume_text)
        
        #Required skills for diffrent roles
        required_skills = {
            "Data Analyst": ["Python","SQL","Excel","Power BI","Pandas","NumPy","Matplotlib","Statistics"
            ],

            "Data Scientist": ["Python","SQL","Pandas","NumPy","Matplotlib","Scikit-learn","Machine Learning","Deep Learning","Statistics"
            ],

            "Machine Learning Engineer": ["Python","SQL","NumPy","Pandas","Scikit-learn","Machine Learning","Deep Learning","TensorFlow","Docker"
            ],

            "Python Developer": ["Python","SQL","Git","GitHub","Flask","Django","Docker"
            ],

            "AI/ML Engineer": ["Python","Machine Learning","Deep Learning","TensorFlow","PyTorch","NLP","Docker"
            ],

            "Business Analyst": ["Excel","SQL","Power BI","Tableau","Statistics"
            ]
        }

            
        role_skills = required_skills[target_role]
        
        # -----------------------------------------
        # Compare Skills
        # -----------------------------------------

        resume_skill_set = {
            skill.lower().strip()
            for skill in resume_skills
}

        found_skills = [
            skill
            for skill in role_skills
            if skill.lower().strip() in resume_skill_set
]

        missing_skills = [
            skill
            for skill in role_skills
            if skill.lower().strip() not in resume_skill_set
]
        
        
        
         # Score
        # -----------------------------------------

        if role_skills:
            skill_match = round(
            (len(found_skills) / len(role_skills)) * 100
    )
        else:
            skill_match = 0
        
        # Results
        # -----------------------------------------

        st.divider()

        st.subheader(
            f"📊 Your {target_role} Skill Profile"
        )


        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric("🎯 Skill Match",f"{skill_match}%",border=True
            )

        with col2:

            st.metric("✅ Skills You Have",len(found_skills),border=True
            )

        with col3:

            st.metric("⚠️ Skills Missing",len(missing_skills),border=True
            )

        st.progress(
            skill_match / 100
        )
        
        #Skills
        # -----------------------------------------

        st.subheader("🧠 Skill Analysis")

        col1, col2 = st.columns(2)


        with col1:

            st.markdown("### ✅ Skills You Have")

            if found_skills:

                for skill in found_skills:

                    st.success(
                        f"✓ {skill}"
                    )

            else:

                st.info(
                    "No required skills detected."
                )


        with col2:

            st.markdown("### ⚠️ Skills You Need")

            if missing_skills:

                for skill in missing_skills:

                    st.warning(
                        f"→ {skill}"
                    )

            else:

                st.success(
                    "🎉 You have all the required skills!"
                )
