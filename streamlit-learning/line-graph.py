
# Graphs:

import streamlit as st
import matplotlib.pyplot as plt # numbers ko graph me show karwana 
import numpy as np

st.title("Line Graph Example")

# Sample data
x = np.linspace(1, 20, 20) 
y = np.random.randint(1, 120, 20)

# Create a figure
fig, ax = plt.subplots()
ax.plot(x, y, marker="o", linestyle="-", color="b", label="Line Graph")
ax.set_title("Simple Line Graph")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.legend()

st.pyplot(fig)
