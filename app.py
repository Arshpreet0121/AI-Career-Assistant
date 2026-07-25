import streamlit as st
from utils import load_css

st.set_page_config(
    page_title="AI Career Assistant",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()

# Hide Streamlit menu/footer
st.markdown("""
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
""", unsafe_allow_html=True)

# ================= HERO =================

st.markdown("""
<div class="hero">
<h1>🚀 AI Career Assistant</h1>
<p class="hero-subtitle">Your AI-powered Career Companion</p>
<p class="hero-text">
Build ATS-friendly resumes, analyze resumes,
match job descriptions, and generate professional
cover letters using Google Gemini AI.
</p>
</div>
""", unsafe_allow_html=True)

# ================= METRICS =================

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("AI Tools", "4")

with m2:
    st.metric("AI Model", "Gemini")

with m3:
    st.metric("Export", "PDF")

with m4:
    st.metric("ATS", "Ready")

st.write("")
st.subheader("🚀 AI Tools")
st.write("")

# ================= FEATURE CARDS =================

# ================= FEATURE CARDS =================

c1, c2 = st.columns(2)

with c1:
    st.markdown("""
    <div class="card">
        <h3>📄 Resume Generator</h3>
        <p>Create ATS-friendly resumes using Gemini AI.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🚀 Launch", key="resume", use_container_width=True):
        st.switch_page("pages/Resume_Generator.py")

with c2:
    st.markdown("""
    <div class="card">
        <h3>📊 ATS Analyzer</h3>
        <p>Analyze your resume and improve ATS score.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🚀 Launch", key="ats", use_container_width=True):
        st.switch_page("pages/ATS_Analyzer.py")

st.write("")

c3, c4 = st.columns(2)

with c3:
    st.markdown("""
    <div class="card">
        <h3>🎯 Job Match</h3>
        <p>Compare your resume with any job description.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🚀 Launch", key="job", use_container_width=True):
        st.switch_page("pages/Job_Match.py")

with c4:
    st.markdown("""
    <div class="card">
        <h3>💌 Cover Letter</h3>
        <p>Generate personalized cover letters instantly.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🚀 Launch", key="cover", use_container_width=True):
        st.switch_page("pages/Cover_Letter.py")