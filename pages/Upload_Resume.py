from services.resume_parser import extract_resume_text
import streamlit as st
from pathlib import Path
from utils import load_css

load_css()

st.set_page_config(
    page_title="Upload Resume",
    page_icon="📂",
    layout="wide"
)

st.title("📂 Upload Resume")

st.write(
    "Upload your resume in PDF or DOCX format."
)

uploaded_file = st.file_uploader(
    "Choose your resume",
    type=["pdf", "docx"]
)

if uploaded_file:

    st.success("Resume uploaded successfully!")

    st.write("### File Details")

    st.write(f"**Filename:** {uploaded_file.name}")

    st.write(f"**File Size:** {round(uploaded_file.size/1024,2)} KB")

    upload_folder = Path("uploads")
    upload_folder.mkdir(exist_ok=True)

    save_path = upload_folder / uploaded_file.name

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"Saved to: {save_path}")

    resume_text = extract_resume_text(str(save_path))

    st.divider()

    st.subheader("📄 Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=350
    )