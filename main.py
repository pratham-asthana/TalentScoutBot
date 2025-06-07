import streamlit as st
from app.ui import show_greeting, collect_user_info, display_questions
from app.prompts import extract_tech_stack, generate_tech_question_prompt
from app.model import load_model

generator = load_model()

st.set_page_config(page_title="TalentScout AI", page_icon="🧠")
st.title("🧠 TalentScout - Hiring Assistant Chatbot")

if "stage" not in st.session_state:
    st.session_state.stage = "greet"
if "info_text" not in st.session_state:
    st.session_state.info_text = ""
if "questions" not in st.session_state:
    st.session_state.questions = ""

if st.session_state.stage == "greet":
    if show_greeting():
        st.session_state.stage = "info"

if st.session_state.stage == "info":
    st.session_state.info_text = collect_user_info()
    if st.button("Submit Info"):
        if "Tech Stack:" in st.session_state.info_text:
            tech_stack = extract_tech_stack(st.session_state.info_text)
            prompt = generate_tech_question_prompt(tech_stack)
            output = generator(prompt, max_length=512)[0]['generated_text']
            st.session_state.questions = output
            st.session_state.stage = "questions"
        else:
            st.warning("⚠️ Please include 'Tech Stack:' in your response.")

if st.session_state.stage == "questions":
    if display_questions(st.session_state.questions):
        for key in st.session_state.keys():
            del st.session_state[key]
