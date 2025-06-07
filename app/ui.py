import streamlit as st
from app.prompts import generate_info_prompt

def show_greeting():
    st.success("👋 Hello! I'm your Hiring Assistant Bot for TalentScout.")
    return st.button("Start Interview")

def collect_user_info():
    st.write(generate_info_prompt())
    return st.text_area("Enter your details here:")

def display_questions(questions):
    st.markdown("### 📋 Technical Questions Based on Your Tech Stack:")
    st.write(questions)
    st.success("✅ Thank you for your time! We will contact you shortly.")
    return st.button("Restart")
