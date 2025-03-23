import streamlit as st
import matplotlib.pyplot as plt

# Streamlit Title
st.title("🥧 Pie Chart - Students' Marks Distribution")

# Data
students = ["Ali", "Umer", "Usman", "Sad", "Zain"]
marks = [20, 40, 70, 90, 30]

# Create Pie Chart
fig, ax = plt.subplots()
ax.pie(marks, labels=students, autopct="%1.1f%%", colors=["red", "blue", "green", "purple", "orange"])

# Title
ax.set_title("Percentage Distribution of Marks")

# Display Graph in Streamlit
st.pyplot(fig)