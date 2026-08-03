# 🤖 AI Resume Screening System

An AI-powered **Resume Screening System** that analyzes resumes against job descriptions using **Natural Language Processing (NLP)** and **Sentence Transformers**. The application calculates an ATS score, identifies missing skills, measures semantic similarity, generates personalized learning recommendations, and creates a downloadable PDF report.

🌐 **Live Demo:** https://ai-resume-screening-system-qfob.onrender.com/

---

## 📌 Features

- 📄 Upload resumes in PDF format
- 📝 Enter any job description
- 🧠 AI-powered semantic similarity using Sentence Transformers
- 🎯 Automatic skill extraction
- 📊 ATS compatibility score calculation
- ✅ Matched & missing skills analysis
- 📚 Personalized learning roadmap
- 📑 Downloadable ATS Report (PDF)
- 💻 Responsive and user-friendly interface
- ☁️ Deployed on Render

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask

### Frontend
- HTML5
- CSS3
- JavaScript

### AI & Machine Learning
- Sentence Transformers
- PyTorch
- Scikit-learn

### Libraries
- PyPDF2
- ReportLab
- NumPy
- Requests

### Deployment
- Git
- GitHub
- Render

---

## 📂 Project Structure

```
AI_Resume_Screening_System/
│
├── dataset/
│   └── skills.txt
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── utils/
│   ├── pdf_generator.py
│   ├── roadmap.py
│   ├── semantic_match.py
│   ├── skill_extraction.py
│   └── text_preprocessing.py
│
├── uploads/
├── app.py
├── requirements.txt
├── runtime.txt
├── README.md
└── .gitignore
```

---

## 🚀 Live Demo

🔗 **Try the application here**

https://ai-resume-screening-system-qfob.onrender.com/

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Akshata-Pattan/AI_Resume_Screening_System.git
```

### Navigate to the project directory

```bash
cd AI_Resume_Screening_System
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Visit:

```
http://127.0.0.1:5000
```

---

## 📖 How It Works

1. Upload a PDF resume.
2. Paste the job description.
3. Extract skills from both resume and job description.
4. Compare them using semantic similarity.
5. Calculate ATS compatibility score.
6. Display:
   - ATS Score
   - Semantic Score
   - Matched Skills
   - Missing Skills
   - Resume Verdict
   - Learning Roadmap
7. Download the ATS report as a PDF.

---

## 🎯 Future Enhancements

- 🔐 User Authentication
- 📊 Resume Analytics Dashboard
- 🤖 AI Resume Improvement Suggestions
- 📁 Resume History
- 📌 Multiple Resume Comparison
- 🌍 Multi-language Resume Support

---

## 📷 Screenshots

> Add screenshots of your application here.

### Home Page

```
screenshots/home.png
```

### Result Page

```
screenshots/result.png
```

### ATS Report

```
screenshots/report.png
```

---

## 🤝 Contributing

Contributions, suggestions, and feature requests are welcome.

If you'd like to contribute:

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---

## 👩‍💻 Author

**Akshata Pattan**

- GitHub: https://github.com/Akshata-Pattan
- LinkedIn: https://www.linkedin.com/in/akshata-pattan-b39832342

---

## ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub.

It helps others discover the project and motivates future improvements.

---

## 📜 License

This project is intended for educational and learning purposes.
