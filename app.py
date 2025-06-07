import streamlit as st
from chatbot import Chatbot

st.set_page_config(page_title="TalentScout Hiring Assistant")

if "bot" not in st.session_state:
    st.session_state.bot = Chatbot()

st.title("TalentScout - AI Hiring Assistant")

user_input = st.text_input("You:", key="input")

if user_input:
    bot = st.session_state.bot
    response = bot.process(user_input)
    st.session_state.history = getattr(st.session_state, "history", []) + [
        ("You", user_input), ("Bot", response)
    ]
    st.experimental_rerun()

# display history
if "history" in st.session_state:
    for speaker, msg in st.session_state.history:
        st.markdown(f"**{speaker}:** {msg}")