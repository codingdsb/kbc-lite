"""
Team Member Name (Roll Number) and respective Contribution:
Darshan Bajeja (2403307): Coding of web and logic part
S Sreelakshmi (2403130): Coding utility functions
Aditya Ambara Matya (2403302): Idea of Project and Content gathering (sports category questions)
Alladi Samuel Abhishek (2403303): Content gathering (India GK category questions)
Hritik Bansal (2403118): Content gathering (Programming category questions)
"""

import streamlit as st
import os
from utils import get_attempt_history, get_questions

st.set_page_config(initial_sidebar_state="collapsed")
st.header("Kaun Banega Crore Pati Lite")

if not os.path.exists("attempts_history.csv"):
    f = open("attempts_history.csv", "w")
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

st.subheader("RULES OF THE QUIZ")

st.write("""
1. You will be given 15 questions.
2. Each correct answer adds up to your points and makes your score equal to the points mentioned below:
    Q1. 1000
    Q2. 2000
    Q3. 3000
    Q4. 5000
    Q5. 10000
    Q6. 20000
    Q7. 40000
    Q8. 80000
    Q9. 160000
    Q10. 320000
    Q11. 640000
    Q12. 1250000
    Q13. 2500000
    Q14. 5000000
    Q15. 10000000
3. If you are above 320000, and give an incorrect answer, you will fall down to 320000 points.
4. If you are above 10000, and give an incorrect answer, you will fall down to 10000 points.
5. If you are below 10000, and give an incorrect answer, you will fall down to 0.
6. You can quit the quiz at any time and get whatever amount of points you have.
""")
