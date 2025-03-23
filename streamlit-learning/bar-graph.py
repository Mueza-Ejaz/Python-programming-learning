
import streamlit as st
import matplotlib.pyplot as plt # numbers ko graph me show karwana 
import numpy as np



st.title("Bar Chart Example")

# Sample data
x = np.arange(1, 4)
y = np.random.randint(10, 100, 3)

# Create a figure
fig, ax = plt.subplots()
ax.bar(x, y, color="r", label="Bar Chart")
ax.set_title("Muezoo Chart")
ax.set_xlabel("Categories")
ax.set_ylabel("Values")
ax.legend()

st.pyplot(fig)

#--------------------------------------------------------------------------


import streamlit as st  # Import Streamlit for web app
import matplotlib.pyplot as plt  # Import Matplotlib for graph

# 🎯 Title of the Streamlit app
st.title("Students' Marks Bar Graph")

# 📊 Data (Student Names & Their Marks)
students = ["Ali", "Umer", "Usman", "Sad", "Zain"]  # X-axis labels
marks = [20, 40, 70, 90, 80]  # Y-axis values

# 🔹 Create a figure & axis for the graph
fig, ax = plt.subplots()

# 🔹 Plot a bar chart
ax.bar(students, marks, color=["red", "blue", "green", "purple", "orange"])

# 🔹 Add labels and title
ax.set_xlabel("Students")  # X-axis label
ax.set_ylabel("Marks out of 100")  # Y-axis label
ax.set_title("Marks of Students in Class")  # Graph title

# 🔹 Show the graph in Streamlit
st.pyplot(fig)


#---------------------------------------------------------------------


import streamlit as lg
import matplotlib.pyplot as plt

lg.title("Students' Subjects Bar Graph")

subjects = ["Math", "English", "Urdu", "Chemistry", "Physics"]
marks = [40, 60, 70, 90, 100]

fig, ax = plt.subplots()
ax.bar(subjects, marks, color=["green", "yellow", "pink", "blue", "purple"])

ax.set_xlabel("Subjects")
ax.set_ylabel("Marks out of 120")
ax.set_title("Subjects Name")

lg.pyplot(fig)


