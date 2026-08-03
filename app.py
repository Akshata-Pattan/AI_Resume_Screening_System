from flask import Flask, render_template, request, send_file
from PyPDF2 import PdfReader
from utils.text_preprocessing import clean_text
from utils.skill_extraction import load_skills, extract_skills
from utils.pdf_generator import generate_pdf
from utils.semantic_match import semantic_similarity
from utils.roadmap import skill_descriptions

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    # Get uploaded resume and job description
    resume = request.files["resume"]
    job_description = request.form["job_description"]

    # Read PDF
    reader = PdfReader(resume)
    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            resume_text += text

    # Clean Resume Text
    resume_text = clean_text(resume_text)

    # Load Skills
    skills = load_skills("dataset/skills.txt")

    # Extract Resume Skills
    found_skills = extract_skills(resume_text, skills)

    # Clean Job Description
    job_description = clean_text(job_description)

    # Extract Job Skills
    job_skills = extract_skills(job_description, skills)

    # Semantic Score
    semantic_score = semantic_similarity(
        resume_text,
        job_description
    )
    semantic_score = round(semantic_score, 2)

    # Matched Skills
    matched_skills = []

    for skill in job_skills:
        if skill in found_skills:
            matched_skills.append(skill)

    # Missing Skills
    missing_skills = []

    for skill in job_skills:
        if skill not in found_skills:
            missing_skills.append(skill)

    # ATS Score
    if len(job_skills) > 0:
        match_score = (len(matched_skills) / len(job_skills)) * 100
    else:
        match_score = 0

    match_score = round(match_score, 2)
        # ==========================
    # AI Learning Roadmap
    # ==========================

    roadmap = []

    for skill in missing_skills:
        roadmap.append({
            "title": f"Learn {skill.title()}",
            "description": skill_descriptions.get(
                skill.title(),
                "Improve this skill to strengthen your resume and ATS score."
            )
        })

    # ==========================
    # Resume Verdict
    # ==========================

    if match_score >= 90:
        verdict = "🌟 Excellent Resume"
        verdict_color = "#22c55e"

    elif match_score >= 75:
        verdict = "👍 Good Resume"
        verdict_color = "#3b82f6"

    else:
        verdict = "📈 Needs Improvement"
        verdict_color = "#ef4444"

    # ==========================
    # AI Recommendations
    # ==========================

    recommendations = []

    for skill in missing_skills:
        recommendations.append(f"Learn {skill.title()}")

    if match_score >= 90:
        recommendations.append(
            "Excellent match! Your resume is highly suitable for this role."
        )
    elif match_score >= 75:
        recommendations.append(
            "Good match. Add a few missing skills to improve your ATS score."
        )
    else:
        recommendations.append(
            "Improve your resume by adding more relevant skills and projects."
        )

    # ==========================
    # Generate PDF
    # ==========================

    generate_pdf(
        "ATS_Report.pdf",
        match_score,
        semantic_score,
        verdict,
        matched_skills,
        missing_skills,
        recommendations
    )

    # ==========================
    # Show Result
    # ==========================

    return render_template(
        "result.html",
        resume_skills=found_skills,
        job_skills=job_skills,
        matched_skills=matched_skills,
        missing_skills=missing_skills,
        match_score=match_score,
        semantic_score=semantic_score,
        matched_count=len(matched_skills),
        missing_count=len(missing_skills),
        total_required=len(job_skills),
        roadmap=roadmap,
        verdict=verdict,
        verdict_color=verdict_color
    )

@app.route("/download")
def download():
    return send_file(
        "ATS_Report.pdf",
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)