import streamlit as st
from utils import load_css

load_css()
from services.resume_parser import extract_resume_text
from services.prompt_builder import build_job_match_prompt
from services.gemini_service import ask_gemini

st.set_page_config(
    page_title="Job Match Analyzer",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 AI Job Match Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=250
)

if uploaded_file and job_description:

    with open(
        f"uploads/{uploaded_file.name}",
        "wb"
    ) as f:

        f.write(uploaded_file.getbuffer())

    resume_text = extract_resume_text(
        f"uploads/{uploaded_file.name}"
    )

    if st.button(
        "Analyze Job Match",
        use_container_width=True
    ):

        prompt = build_job_match_prompt(
            resume_text,
            job_description
        )

        with st.spinner("🤖 Comparing Resume..."):

            response = ask_gemini(prompt)

        if "currently busy" in response.lower():

            st.warning(response)

        else:

            st.success("Analysis Complete!")

            st.markdown(response)