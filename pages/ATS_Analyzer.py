import streamlit as st
import os
import re
import uuid

from utils import load_css
from services.resume_parser import extract_resume_text
from services.prompt_builder import build_ats_prompt
from services.gemini_service import ask_gemini

load_css()

st.title("📊 ATS Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

if uploaded_file:

    st.success("Resume Uploaded!")

    # Create uploads directory if it doesn't exist
    os.makedirs("uploads", exist_ok=True)

    # Generate a unique filename
    file_extension = os.path.splitext(uploaded_file.name)[1]
    file_name = f"{uuid.uuid4().hex}{file_extension}"

    file_path = os.path.join("uploads", file_name)

    # Save uploaded resume
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    try:

        # Extract resume text
        resume_text = extract_resume_text(file_path)

        if not resume_text:
            st.error("Unable to extract text from this resume.")

        else:

            if st.button("Analyze Resume"):

                prompt = build_ats_prompt(resume_text)

                with st.spinner("Analyzing Resume..."):

                    response = ask_gemini(prompt)

                if not response:
                    st.error("Unable to generate analysis. Please try again.")

                elif "currently busy" in response.lower():

                    st.warning(response)

                else:

                    # Extract ATS Score
                    score = None

                    match = re.search(
                        r'(\d{1,3})\s*/\s*100',
                        response
                    )

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

                    # Display Score
                    if score is not None:

                        score = min(max(score, 0), 100)

                        st.metric(
                            "📊 ATS Score",
                            f"{score}%"
                        )

                        st.progress(score / 100)

                    st.markdown("---")

                    # Display Analysis
                    st.markdown(response)

    except Exception as e:

        st.error(f"An error occurred: {str(e)}")