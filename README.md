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

# 🚀 How to Run This Project Locally

## Step 1: Clone Repository

```bash
git clone https://github.com/your-username/resume-ats-ai.git
```

---

## Step 2: Move into Project Folder

```bash
cd resume-ats-ai
```

---

## Step 3: Create Virtual Environment

### Using Conda

```bash
conda create -p atsenv python==3.10 -y
```

Activate Environment:

```bash
conda activate atsenv/
```

---

### OR Using venv

```bash
python -m venv venv
```

Activate Environment (Windows):

```bash
venv\Scripts\activate
```

---

## Step 4: Create `requirements.txt`

Add important libraries and frameworks inside `requirements.txt`

Example:

```txt
streamlit
google-generativeai
python-dotenv
PyPDF2
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔐 Create `.env` File

Create a `.env` file inside the project folder to securely store API key.

```env
GOOGLE_API_KEY='YOUR_API_KEY'
```

---

# 🔑 Generate Gemini API Key

- Open Browser
- Search: **Makersuite / Google AI Studio**
- Sign Up
- Click **Create API Key**
- Copy API Key
- Paste inside `.env`

---

# 🌐 Workflow of Website

```text
Setup Poppler
      ↓
API Integration
      ↓
PDF to Text Extraction (PyPDF2)
      ↓
Pass Text to Gemini API
      ↓
Return ATS Response
```

---

# 🖥️ Create `app.py`

## Main Functionalities

- Import all required libraries
- Create `get_gemini_response()` function
- Create `input_pdf_text()` function
- Create `prompt_input` template
- Build basic Streamlit UI

---

# ▶️ Run the Application

Open CMD / Terminal

Go to project folder where `app.py` exists.

Run:

```bash
streamlit run app.py
```

---

# 🌐 Open in Browser

```text
http://localhost:8501
```
