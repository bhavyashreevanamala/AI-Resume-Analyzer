from flask import Flask, render_template, request
import os
import webbrowser
from resume_parser import extract_text, extract_skills

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():

    if 'resume' not in request.files:
        return "No File Uploaded"

    file = request.files['resume']

    if file.filename == '':
        return "No Selected File"

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    text = extract_text(filepath)
    skills = extract_skills(text)

    ats_score = min(len(skills) * 10, 100)

    suggestions = [
    "Add more AI projects",
    "Improve resume formatting",
    "Add certifications",
    "Add internship experience"
]

    if "Python" not in skills:
        suggestions.append("Add Python skill")

    if "JavaScript" not in skills:
        suggestions.append("Add JavaScript skill")

    if len(skills) < 5:
        suggestions.append("Add more technical skills")

    return render_template(
        'index.html',
        skills=skills,
        ats_score=ats_score,
        suggestions=suggestions
    )

if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True)