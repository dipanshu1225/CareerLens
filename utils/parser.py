from pypdf import PdfReader

def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text= ""
    
    for page in reader.pages:
        page_text = page.extract_text()
        
        if page_text:
            text+= page_text + "\n"
    
    return text

#skill
SKILLS = [
    "Python",
    "SQL",
    "Excel",
    "Power BI",
    "Tableau",
    "Pandas",
    "NumPy",
    "Matplotlib",
    "Seaborn",
    "Scikit-learn",
    "Machine Learning",
    "Deep Learning",
    "TensorFlow",
    "PyTorch",
    "NLP",
    "Flask",
    "Streamlit",
    "Django",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "Git",
    "GitHub",
    "MySQL",
    "MongoDB",
    "AWS",
    "Docker"
]

def detect_skills(text):
    text_lower = text.lower()
    
    found_skills = []
    
    for skill in SKILLS:
        if skill.lower() in text_lower:
            found_skills.append(skill)
        
    return found_skills
        
