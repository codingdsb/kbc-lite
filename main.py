"""
Team Member Name (Roll Number) and respective Contribution:
Darshan Bajeja (2403307): Coding of web and logic part
S Sreelakshmi: Coding utility functions
Aditya Ambara Matya: Idea of Project and Content gathering (sports category questions)
Alladi Samuel Abhishek: Content gathering (India GK category questions)
Hritik Bansal: Content gathering (Programming category questions)
"""

import streamlit as st
import os
from utils import get_attempt_history, get_questions

st.set_page_config(initial_sidebar_state="collapsed")
st.header("Kaun Banega Crore Pati Lite")

if not os.path.exists("attempt_history.csv"):
    f = open("attempt_history.csv", "w")
    f.close()

ATTEMPT_HISTORY = get_attempt_history()


username = st.text_input("What should we call you? Please enter a username:")
start_quiz_button = st.button("Start Quiz")


if start_quiz_button:
    if username != "":
        for attempt in ATTEMPT_HISTORY:
            if attempt["username"] == username:
                st.write(
                    f"Username {username} already taken, please choose another username."
                )
                break
        else:
            st.session_state.username = username
            st.session_state.questions = get_questions()
            st.session_state.current_question = 0
            st.session_state.points = 0
            st.session_state.quiz_status = "NONE"
            st.switch_page("pages/quiz.py")
    else:
        st.subheader("Please choose a username")

leaderboard_button = st.button("See Leaderboard")
if leaderboard_button:
    st.switch_page("pages/leaderboard.py")
