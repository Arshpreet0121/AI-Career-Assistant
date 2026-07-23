import streamlit as st

from utils import load_css
load_css()

from services.resume_parser import extract_resume_text
from services.prompt_builder import build_cover_letter_prompt
from services.gemini_service import ask_gemini
from services.pdf_service import create_resume_pdf

st.set_page_config(
    page_title="Cover Letter",
    page_icon="💌",
    layout="wide"
)

st.title("💌 AI Cover Letter Generator")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf","docx"]
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
        "Generate Cover Letter",
        use_container_width=True
    ):

        prompt = build_cover_letter_prompt(
            resume_text,
            job_description
        )

        with st.spinner("Writing Cover Letter..."):

            response = ask_gemini(prompt)

        if "currently busy" in response.lower():

            st.warning(response)

        else:

            st.success("Cover Letter Generated!")

            st.markdown(response)

            pdf_file = create_resume_pdf(response)

            with open(pdf_file, "rb") as file:

                st.download_button(
                    "📄 Download Cover Letter",
                    file,
                    file_name="cover_letter.pdf",
                    mime="application/pdf"
                )