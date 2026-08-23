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
    
import re    
def detect_experience(resume_text):

    text = resume_text.lower()

    patterns = [
        r'(\d+(?:\.\d+)?)\+?\s*years?\s*(?:of)?\s*(?:professional\s*)?experience',
        r'(\d+(?:\.\d+)?)\+?\s*yrs?\s*(?:of)?\s*(?:professional\s*)?experience'
    ]

    years = []

    for pattern in patterns:
        matches = re.findall(pattern, text)

        for match in matches:
            years.append(float(match))

    if years:

        max_years = max(years)

        if max_years == 0:
            return "Fresher"

        if max_years.is_integer():
            return f"{int(max_years)} Years"

        return f"{max_years} Years"

    fresher_words = [
        "fresher",
        "fresh graduate",
        "recent graduate",
        "no experience",
        "no professional experience",
        "entry level",
        "entry-level"
    ]

    for word in fresher_words:
        if word in text:
            return "Fresher"

    return "Fresher"