import streamlit as st
from services.pdf_service import create_resume_pdf
from utils import load_css

load_css()
from services.prompt_builder import build_resume_prompt
from services.gemini_service import ask_gemini

st.set_page_config(
    page_title="Resume Generator",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Generator")

st.write(
    "Fill in your information and let Gemini create an ATS-friendly resume."
)

with st.form("resume_form"):

    st.subheader("👤 Personal Information")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")

    with col2:
        linkedin = st.text_input("LinkedIn")
        github = st.text_input("GitHub")
        location = st.text_input("Location")

    st.divider()

    st.subheader("🎓 Education")
    education = st.text_area("Education", height=120)

    st.subheader("💼 Experience")
    experience = st.text_area("Experience", height=150)

    st.subheader("🚀 Projects")
    projects = st.text_area("Projects", height=150)

    st.subheader("🛠 Skills")
    skills = st.text_area("Skills (comma separated)")

    st.subheader("🏆 Certifications")
    certifications = st.text_area("Certifications")

    st.subheader("🎖 Achievements")
    achievements = st.text_area("Achievements")

    generate = st.form_submit_button(
        "🚀 Generate Resume",
        use_container_width=True
    )

if generate:

    data = {
        "name": name,
        "email": email,
        "phone": phone,
        "linkedin": linkedin,
        "github": github,
        "location": location,
        "education": education,
        "experience": experience,
        "projects": projects,
        "skills": skills,
        "certifications": certifications,
        "achievements": achievements
    }

    prompt = build_resume_prompt(data)

    with st.spinner("🤖 Gemini is creating your ATS Resume..."):
        response = ask_gemini(prompt)

    if "currently busy" in response.lower():

        st.warning(response)

    else:

        st.success("✅ Resume Generated!")

        st.markdown(response)

        pdf_file = create_resume_pdf(response)

        with open(pdf_file, "rb") as file:

            st.download_button(
                label="📥 Download Resume as PDF",
                data=file,
                file_name="AI_Resume.pdf",
                mime="application/pdf",
                use_container_width=True
            )