import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json
import re

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("GOOGLE_API_KEY not found")
    st.stop()

genai.configure(api_key=api_key)

MODELS = {
    "pro": "gemini-2.5-flash",
    "flash": "gemini-2.5-flash"
}


def get_gemini_response(prompt, model_choice="pro"):
    try:
        model_name = MODELS.get(model_choice, "gemini-2.5-flash")

        model = genai.GenerativeModel(
            model_name=model_name,
            generation_config={
                "temperature": 0.2,
                "max_output_tokens": 2048,
                "top_p": 0.95,
            }
        )

        response = model.generate_content(prompt)

        return response.text.strip() if response and response.text else ""

    except Exception as e:
        error_str = str(e).lower()

        if "429" in error_str or "quota" in error_str:
            st.error("Quota limit exceeded")
        else:
            st.error(f"Model Error: {str(e)}")

        return None


def input_pdf_text(uploaded_file):
    try:
        reader = pdf.PdfReader(uploaded_file)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text[:15000]

    except Exception as e:
        return f"PDF_ERROR: {str(e)}"


input_prompt = """
You are an expert ATS (Application Tracking System) reviewer.

Analyze the resume against the job description carefully.

Return ONLY valid JSON.

{
  "JD Match": "85%",
  "MissingKeywords": ["python", "sql", "aws"],
  "Profile Summary": "Short professional summary",
  "Strengths": ["point 1", "point 2"],
  "Weaknesses": ["point 1", "point 2"]
}

Resume:
{resume}

Job Description:
{jd}
"""


def safe_extract_json(response_text):
    if not response_text:
        return None

    try:
        return json.loads(response_text)

    except:
        try:
            match = re.search(r'\{.*\}', response_text, re.DOTALL)

            if match:
                cleaned = match.group(0)

                cleaned = re.sub(r',\s*}', '}', cleaned)
                cleaned = re.sub(r',\s*\]', ']', cleaned)

                return json.loads(cleaned)

        except:
            pass

    return None


st.set_page_config(page_title="AI ATS System", layout="centered")

st.title("AI ATS SYSTEM")
st.caption("Gemini Powered Resume Analyzer")

jd = st.text_area("Paste Job Description", height=220)

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type="pdf"
)

model_choice = st.radio(
    "Select Model",
    ["pro", "flash"],
    format_func=lambda x: "Gemini 2.5 Flash"
)

submit = st.button("Analyze Resume", type="primary")


if submit:

    if not jd.strip():
        st.warning("Please enter Job Description")

    elif uploaded_file is None:
        st.warning("Please upload Resume PDF")

    else:

        with st.spinner("Analyzing Resume..."):

            text = input_pdf_text(uploaded_file)

            if text.startswith("PDF_ERROR"):
                st.error(text)
                st.stop()

            final_prompt = input_prompt.replace(
                "{resume}", text
            ).replace(
                "{jd}", jd
            )

            response_text = get_gemini_response(
                final_prompt,
                model_choice
            )

            if response_text:

                st.subheader("ATS Analysis Result")

                result = safe_extract_json(response_text)

                if result:

                    st.json(result)

                    with st.expander("Raw Response"):
                        st.text(response_text)

                else:

                    st.error("Invalid JSON format")

                    st.text_area(
                        "Raw Output",
                        response_text,
                        height=400
                    )