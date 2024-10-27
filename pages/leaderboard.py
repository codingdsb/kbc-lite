import streamlit as st
from utils import get_attempt_history
import matplotlib.pyplot as plt

st.header("KBC Lite- Leader Board")

attempt_history = get_attempt_history()

# sort by points
attempt_history.sort(key=lambda k: k["points"], reverse=True)
scores = [attempt["points"] for attempt in attempt_history]
attempt_history = attempt_history[:10]
st.dataframe(attempt_history)

# Displaying attempt chart


x = [
    0,
    1000,
    2000,
    5000,
    10000,
    20000,
    40000,
    80000,
    160000,
    320000,
    640000,
    1250000,
    2500000,
    5000000,
    10000000,
]

labels = [str(score) for score in x]

y = [scores.count(score) for score in x]

fig = plt.figure(figsize=(10, 5))
plt.xticks(x, labels=labels, rotation="vertical")
plt.plot(x, y, color="green")
plt.xlabel("Points")
plt.ylabel("Number of people")


plt.title("Leader Board")
st.pyplot(fig)
