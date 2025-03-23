import streamlit as st
import matplotlib.pyplot as plt

# Streamlit Title
st.title("📈 Line Graph - Students' Marks")

# Data
students = ["Ali", "Umer", "Usman", "Sad", "Zain"]
marks = [20, 40, 70, 90, 30]

# Create Line Graph
fig, ax = plt.subplots()
ax.plot(students, marks, marker="o", linestyle="-", color="b", linewidth=2, markersize=8)

# Labels & Title
ax.set_xlabel("Students")
ax.set_ylabel("Marks out of 100")
ax.set_title("Marks Trend of Students")

# Display Graph in Streamlit
st.pyplot(fig)

