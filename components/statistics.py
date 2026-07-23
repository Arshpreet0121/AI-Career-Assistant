import streamlit as st


def show_statistics():

    st.subheader("📈 Quick Statistics")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("🤖 AI Model", "Gemini")

    col2.metric("📄 Documents", "0")

    col3.metric("📊 ATS Engine", "Ready")

    col4.metric("⚡ Version", "1.0")