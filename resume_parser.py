import PyPDF2
import docx

SKILLS_DB = [
    "Python",
    "Java",
    "JavaScript",
    "HTML",
    "CSS",
    "React",
    "Node.js",
    "Flask",
    "Django",
    "MongoDB",
    "SQL",
    "AI",
    "Machine Learning",
    "Cloud Computing",
    "Cybersecurity"
]

def extract_text(file_path):

    text = ""

    if file_path.endswith('.pdf'):

        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)

            for page in reader.pages:
                text += page.extract_text()

    elif file_path.endswith('.docx'):

        doc = docx.Document(file_path)

        for para in doc.paragraphs:
            text += para.text

    return text


def extract_skills(text):

    found_skills = []

    for skill in SKILLS_DB:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills