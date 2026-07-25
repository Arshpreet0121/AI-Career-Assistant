import streamlit as st

def card(icon, title, desc):
    with st.container(border=True):
        st.markdown(f"## {icon} {title}")
        st.write(desc)
        st.button("Open Tool", key=title)

def show_feature_cards():
    col1, col2 = st.columns(2)

    with col1:
        card(
            "📄",
            "Resume Generator",
            "Generate ATS-friendly resumes using Gemini AI."
        )

    with col2:
        card(
            "📊",
            "ATS Analyzer",
            "Analyze your resume and improve ATS score."
        )

    col3, col4 = st.columns(2)

    with col3:
        card(
            "🎯",
            "Job Match",
            "Compare your resume with any job description."
        )

    with col4:
        card(
            "💌",
            "Cover Letter",
            "Generate professional cover letters instantly."
        )