
import streamlit as st
from utils import load_css

load_css()

st.set_page_config(
    page_title="AI Career Assistant",
    page_icon="🚀",
    layout="wide"
)

# ==========================
# HERO SECTION
# ==========================

st.markdown("""
<div class="hero">

<h1>🚀 AI Career Assistant</h1>

<h3>Your AI-powered Career Companion</h3>

<p>
Create ATS-friendly resumes,
analyze resumes,
match job descriptions,
and generate professional cover letters.
</p>

</div>
""", unsafe_allow_html=True)

# ==========================
# FEATURE CARDS
# ==========================

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
<div class="card">

## 📄 Resume Generator

Generate ATS optimized resumes using Gemini AI.

</div>
""", unsafe_allow_html=True)

with col2:

    st.markdown("""
<div class="card">

## 📊 ATS Analyzer

Analyze your resume and improve ATS score.

</div>
""", unsafe_allow_html=True)

# ==========================
# SECOND ROW
# ==========================

col3, col4 = st.columns(2)

with col3:

    st.markdown("""
<div class="card">

## 🎯 Job Match

Compare your resume with any job description.

</div>
""", unsafe_allow_html=True)

with col4:

    st.markdown("""
<div class="card">

## 💌 Cover Letter

Generate personalized cover letters in seconds.

</div>
""", unsafe_allow_html=True)