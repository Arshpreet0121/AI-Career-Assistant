<<<<<<< HEAD
# AI-Career-Assistant
An AI-powered Career Assistant built with Python, Streamlit, and Google Gemini AI for ATS-friendly resume generation, resume analysis, job matching, and cover letter creation.
=======
# 🚀 AI Career Assistant

An AI-powered Career Assistant built with **Python**, **Streamlit**, and **Google Gemini AI** that helps users create ATS-friendly resumes, analyze resumes, match resumes with job descriptions, and generate professional cover letters.

---

## ✨ Features

### 📄 AI Resume Generator
- Generate ATS-friendly resumes using Google Gemini AI
- Professional formatting
- ATS optimized content
- PDF download support

### 📊 ATS Resume Analyzer
- Analyze resume quality
- ATS score estimation
- Strengths & weaknesses
- Missing keywords
- Improvement suggestions

### 🎯 Job Match Analyzer
- Compare resume with any job description
- Match score
- Matching skills
- Missing skills
- Interview readiness
- Personalized recommendations

### 💌 AI Cover Letter Generator
- Generates professional cover letters
- Personalized for each job description
- Formal business format
- PDF download support

### 📂 Resume Upload
- Upload PDF or DOCX resumes
- Extract resume text automatically
- View parsed resume content

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI
- Google Gemini API

### Libraries
- PyMuPDF
- python-docx
- ReportLab
- python-dotenv

---

## 📁 Project Structure

```
AI_Career_Assistant/
│
├── app.py
├── requirements.txt
├── .env
├── assets/
│   └── style.css
├── pages/
│   ├── Home.py
│   ├── Resume_Generator.py
│   ├── ATS_Analyzer.py
│   ├── Job_Match.py
│   ├── Cover_Letter.py
│   ├── Upload_Resume.py
│   └── Settings.py
├── services/
│   ├── gemini_service.py
│   ├── pdf_service.py
│   ├── prompt_builder.py
│   └── resume_parser.py
└── uploads/
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/AI_Career_Assistant.git
```

### Navigate into the project

```bash
cd AI_Career_Assistant
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run the application

```bash
python -m streamlit run app.py
```

---

## 📷 Screenshots

Add screenshots of:

- Home Dashboard
- Resume Generator
- ATS Analyzer
- Job Match Analyzer
- Cover Letter Generator

---

## 🚀 Future Improvements

- Resume History
- Multiple Resume Templates
- Login & Authentication
- Export to DOCX
- Interview Question Generator
- AI Career Roadmap
- Resume Keyword Optimizer
- Multi-language Support

---

## 👨‍💻 Author

**Arshpreet Singh**

Built using Python, Streamlit, and Google Gemini AI.

---

## 📄 License

This project is licensed under the MIT License.
>>>>>>> 264c40f (Final AI Career Assistant)
