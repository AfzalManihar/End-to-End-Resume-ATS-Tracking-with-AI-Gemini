import streamlit as st
import google.generativeai as genai
import PyPDF2 as pdf
import json
import re

st.set_page_config(
    page_title="AI ATS System",
    layout="centered"
)

# ---------------- API KEY ----------------

try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)

except Exception:
    st.error("GOOGLE_API_KEY not found in Streamlit Secrets")
    st.stop()

# ---------------- MODELS ----------------

MODELS = {
    "pro": "gemini-2.5-flash",
    "flash": "gemini-2.5-flash"
}

# ---------------- GEMINI RESPONSE ----------------

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

        if response and response.text:
            return response.text.strip()

        return ""

    except Exception as e:

        error_message = str(e)

        if "429" in error_message.lower():
            st.error("Quota limit exceeded. Try again later.")
        else:
            st.error(f"Model Error: {error_message}")

        return None

# ---------------- PDF EXTRACTION ----------------

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

# ---------------- PROMPT ----------------

input_prompt = """
You are an expert ATS (Applicant Tracking System) reviewer.

Analyze the resume against the job description.

Return ONLY valid JSON.

Do not use markdown.
Do not use ```json.

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

# ---------------- JSON EXTRACTION ----------------

def safe_extract_json(response_text):

    if not response_text:
        return None

    try:

        cleaned = response_text.strip()

        cleaned = cleaned.replace("```json", "")
        cleaned = cleaned.replace("```", "")

        start = cleaned.find("{")
        end = cleaned.rfind("}") + 1

        if start != -1 and end != -1:

            json_text = cleaned[start:end]

            json_text = re.sub(r",\s*}", "}", json_text)
            json_text = re.sub(r",\s*\]", "]", json_text)

            return json.loads(json_text)

    except Exception:
        return None

    return None

# ---------------- UI ----------------

st.title("AI ATS SYSTEM")

st.caption("Gemini Powered Resume ATS Analyzer")

jd = st.text_area(
    "Paste Job Description",
    height=220
)

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type="pdf"
)

model_choice = st.radio(
    "Select Model",
    ["pro", "flash"],
    format_func=lambda x: "Gemini 2.5 Flash"
)

submit = st.button(
    "Analyze Resume",
    type="primary"
)

# ---------------- MAIN LOGIC ----------------

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
                "{resume}",
                text
            ).replace(
                "{jd}",
                jd
            )

            response_text = get_gemini_response(
                final_prompt,
                model_choice
            )

            if response_text:

                st.subheader("ATS Analysis Result")

                result = safe_extract_json(response_text)

                if result:

                    st.success("Analysis Completed")

                    st.json(result)

                    with st.expander("Raw Response"):
                        st.text(response_text)

                else:

                    st.warning("Could not parse JSON correctly")

                    cleaned_response = response_text.replace(
                        "```json",
                        ""
                    ).replace(
                        "```",
                        ""
                    )

                    st.text_area(
                        "Model Output",
                        cleaned_response,
                        height=400
                    )

                    
