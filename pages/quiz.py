import streamlit as st


if (
    "username" not in st.session_state.keys()
    or "questions" not in st.session_state.keys()
):
    st.switch_page("main.py")

index_vs_points = {
    0: 1000,
    1: 2000,
    2: 3000,
    3: 5000,
    4: 10000,
    5: 20000,
    6: 40000,
    7: 80000,
    8: 160000,
    9: 320000,
    10: 640000,
    11: 1250000,
    12: 2500000,
    13: 5000000,
    14: 10000000,
}


st.header(f"Kaun Banega Crore Pati Lite")

questions = st.session_state.questions

st.divider()


def show_question(idx):
    st.subheader(questions[idx]["question"])
    st.write("Category: " + questions[idx]["category"])
    st.write(f"For {index_vs_points[idx]} points")
    user_ans = st.radio(
        "Choose an option", questions[idx]["options"], key=questions[idx]
    )

    if st.button(f"{user_ans} को लॉक किया जाए", key=idx):
        if user_ans == questions[idx]["answer"]:
            st.session_state.points = index_vs_points[idx]
            st.write(f"Correct! You have {st.session_state.points} points now.")
            if idx < len(questions) - 1:
                st.session_state.current_question += 1

            else:
                st.session_state.quiz_status = "WON"

        else:
            if st.session_state.points >= 320000:
                st.session_state.points = 320000
            elif st.session_state.points >= 10000:
                st.session_state.points = 10000
            else:
                st.session_state.points = 0

            st.session_state.quiz_status = "LOST"
        st.rerun()

if st.session_state.quiz_status == "WON":
    st.subheader(
        "Congratulations! You have won the quiz. Your score is: "
        + str(st.session_state.points)
    )
    with open("attempts_history.csv", "a") as f:
        f.write(st.session_state.username + "," + str(st.session_state.points) + "\n")

        st.session_state.quiz_status = "DONE"

elif st.session_state.quiz_status == "LOST":
    st.subheader(
        "You have lost the quiz. Your score is: " + str(st.session_state.points)
    )
    with open("attempts_history.csv", "a") as f:
        f.write(st.session_state.username + "," + str(st.session_state.points) + "\n")

        st.session_state.quiz_status = "DONE"

elif st.session_state.quiz_status == "QUIT":
    st.subheader(
        "Thank you for playing. Your score is: " + str(st.session_state.points)
    )
    with open("attempts_history.csv", "a") as f:
        f.write(st.session_state.username + "," + str(st.session_state.points) + "\n")

        st.session_state.quiz_status = "DONE"

elif st.session_state.quiz_status == "DONE":
    st.switch_page("main.py")

else:
    st.subheader("Username: " + st.session_state.username)
    st.subheader("Points: " + str(st.session_state.points))

    quit_button = st.button("Quit")
    if quit_button:
        st.session_state.quiz_status = "QUIT"
        st.rerun()

    show_question(st.session_state.current_question)
