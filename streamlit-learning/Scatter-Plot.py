import streamlit as st
import matplotlib.pyplot as plt

# Streamlit Title
st.title("🔴 Scatter Plot - Students' Marks")

# Data
students = ["Ali", "Umer", "Usman", "Sad", "Zain"]
marks = [20, 40, 70, 90, 30]

# Create Scatter Plot
fig, ax = plt.subplots()
ax.scatter(students, marks, color="green", s=100)

# Labels & Title
ax.set_xlabel("Students")
ax.set_ylabel("Marks out of 100")
ax.set_title("Scatter Plot of Student Marks")

# Display Graph in Streamlit
st.pyplot(fig)