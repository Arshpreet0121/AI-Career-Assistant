import streamlit as st
from utils import load_css

load_css()
from services.resume_parser import extract_resume_text
from services.prompt_builder import build_ats_prompt
from services.gemini_service import ask_gemini
import re
            
        

st.title("📊 ATS Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

if uploaded_file:

    st.success("Resume Uploaded!")

    with open(
        f"uploads/{uploaded_file.name}",
        "wb"
    ) as f:

        f.write(uploaded_file.getbuffer())

    resume_text = extract_resume_text(
        f"uploads/{uploaded_file.name}"
    )

    if st.button("Analyze Resume"):

        prompt = build_ats_prompt(resume_text)

        with st.spinner("Analyzing Resume..."):

           response = ask_gemini(prompt)

        score = None

        match = re.search(r'(\d{1,3})\s*/\s*100', response)

        if match:
            score = int(match.group(1))
        else:
            match = re.search(
                r'ATS Score.*?(\d{1,3})',
                response,
                re.IGNORECASE
            )
            if match:
                score = int(match.group(1))

        if "currently busy" in response.lower():

            st.warning(response)

        else:

            if score:

                st.metric(
                    "📊 ATS Score",
                    f"{score}%"
                )

                st.progress(score / 100)

            st.markdown("---")

            st.markdown(response)