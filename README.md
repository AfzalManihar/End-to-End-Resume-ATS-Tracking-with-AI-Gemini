# 📄 End-to-End Resume ATS Tracking System using AI (Google Gemini Pro)

---

## 🧠 Introduction

The **Resume ATS Tracking System using AI** is an end-to-end AI-powered web application that evaluates a candidate’s resume against a job description and provides an **ATS compatibility score, missing keywords, and profile improvement suggestions**.

This project uses **Google Gemini Pro (LLM)** along with **Streamlit** to build an intelligent resume screening system similar to modern Applicant Tracking Systems used in companies.

It demonstrates a complete AI workflow:

**PDF Processing → Text Extraction → Prompt Engineering → LLM Analysis → Structured JSON Output → Web Deployment**

---

## 🌐 Live Demo

👉 Streamlit App: *(Add your deployed link here)*  
Example: https://your-app-name.streamlit.app/

📌 Upload resume and job description to get instant ATS analysis in real-time.

---
## Project Structure 
resume-ats-ai/
│
├── app.py                # Main Streamlit application
├── .env                  # API keys (not pushed to GitHub)
├── requirements.txt     # Dependencies
└── README.md            # Project documentation

---
## 🎯 Problem Statement

In today’s competitive job market:

- Recruiters receive thousands of resumes
- Manual screening is slow and inefficient
- Candidates often don’t know why they are rejected

### This project solves:

✔ Resume-job matching analysis  
✔ ATS score estimation  
✔ Missing skill identification  
✔ AI-based profile improvement suggestions  

---

## ✨ Key Features

- 🔍 Upload resume in PDF format  
- 🧠 AI-powered ATS analysis using Google Gemini  
- 📊 Job Description vs Resume matching score  
- 📌 Extract missing keywords  
- 🧾 Professional profile summary generation  
- ⚡ Real-time results in Streamlit UI  
- 📄 JSON structured output for clarity  

---

## ⚙️ How It Works

1. User uploads resume (PDF format)  
2. User pastes Job Description  
3. System extracts text from resume  
4. Prompt is sent to **Google Gemini Pro (LLM)**  
5. AI analyzes:
   - Skill match  
   - Keyword gaps  
   - Profile quality  
6. Output is displayed in structured format:
   - JD Match %
   - Missing Keywords
   - Profile Summary  

---

## 🛠️ Tools & Technologies Used

- 🐍 Python  
- 📄 PyPDF2 – PDF text extraction  
- 🤖 Google Gemini Pro (LLM)  
- 🌐 Streamlit – Web application  
- 🧠 Prompt Engineering  
- 🔧 python-dotenv – Environment variable management  
- 📦 JSON – Structured AI output handling  

---

## 🚀 How to Run This Project Locally

```bash
# Step 1: Clone repository
git clone https://github.com/your-username/resume-ats-ai.git

# Step 2: Move into project folder
cd resume-ats-ai

# Step 3: Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

# Step 4: Install dependencies
pip install -r requirements.txt

# Step 5: Add API Key in .env file
GOOGLE_API_KEY=your_api_key_here

# Step 6: Run Streamlit app
streamlit run app.py

