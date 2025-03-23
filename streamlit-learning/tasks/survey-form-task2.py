# 15 minutes website using python with streamlit:

# - main heading(Survey form)
# -subheading(No.of population in each provinces)
# - 4 input fields(sindh,punjab,blochistan,kpk)
# - button(submit)- show population through bar graph
# - subheading(Age grouped based in pakistan)
# - 4 slider(child agr group,tean age group,adult age group, senior citizens age group)
# - button(click) show data in pie chart graph
# - subheading(gender wise population)
# - praragraph
# - dropdown(male,female,other) usk hi braber me aik input field hogi- submit button
# - print graph button (show bar graph)


# font-family: Arial, sans-serif;
# font-family: Verdana, sans-serif;
# font-family: Georgia, serif;
# font-family: 'Times New Roman', serif;
# font-family: 'Courier New', monospace;
# font-family: Tahoma, sans-serif;
# font-family: Trebuchet MS, sans-serif;

import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Survey Form", page_icon="👧", layout="centered" ) 

def custom_css():
    st.markdown(
        """
        <style>
          
           @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        /* Applying font to the entire app */
            html, body, [class*="st-"] {
           font-family: Georgia, serif; /* Applying Poppins font */
        }

        .stApp{
            background-image: url("https://images.unsplash.com/photo-1487700160041-babef9c3cb55?q=80&w=1452&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
            z-index:-1;
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            color: black;
            text-align: center;
        }

        .stApp > div {
        backdrop-filter: blur(5px); /* Prevents blur on text */
    }

        .stheader {
        font-family: Verdana, sans-serif; !important 
        font-size: 30px;
        color: #4CAF50; /* Green */
        text-align: left;
        }


        .stsubheader {
        font-family: 'Courier New', monospace; !important 
        font-size: 30px;
        color: #4CAF50; /* Green */
        text-align: left;
        }

        label {
        color: black !important; /* Changing label color to green */
        font-size: 18px; /* Increasing font size */
        font-weight: bold; /* Making it bold */
    }
    
   input[type=number] {
        border-radius: 10px 0px 10px 0px !important; /* Rounded corners */
        border: 2px solid #3498db !important; /* Blue border */
        padding: 10px !important;
        font-size: 16px !important;
        background: rgba(255, 255, 255, 0.8) !important; /* Semi-transparent background */
        color: black !important;
        outline: none !important;
    }




    .stButton > button {
        background-color: blue !important; /* Change button background to blue */
        color: white !important; /* Change text color to white */
        font-size: 18px; /* Increase font size */
        border-radius: 10px 0px 10px 0px; /* Rounded corners */
        padding: 10px 20px; /* Add padding */
        border: 2px solid black; /* Black border */
    }

    /* Change button color when hovered */
    .stButton > button:hover {
        background-color: darkblue !important; /* D
    }

    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        font-weight: bold;
        color: #333;
    }

        </style>

        """,

        unsafe_allow_html=True,
    )

custom_css()

st.header("*SURVEY FORM*")
st.subheader("_Province Population_")

# Input fields:

sindh = st.number_input("Sindh Population", max_value=59696147, value=55696147)
punjab = st.number_input("Punjab Population", max_value=137688922, value=127688922)
balochistan = st.number_input("Balochistan Population",  max_value=20000000, value=15000000)
kpk = st.number_input("KPK Population", max_value=80000000, value=40000000)

# Submit button
if st.button("Show Population Graph"):
    st.title("Province Population Bar Graph")


    p_names = ["Sindh", "KPK", "Balochistan", "Punjab"]
    provinces = [sindh, kpk, balochistan, punjab]

    fig, ax = plt.subplots()
    ax.bar(p_names, provinces, color=["blue", "yellow", "black", "green"])

    ax.set_xlabel("Provinces")
    ax.set_ylabel("No.of population in each provinces")
    ax.set_title(" Province Bar Graph")

    # Disable scientific notation on y-axis
    ax.ticklabel_format(style='plain', axis='y')

    st.pyplot(fig)

#---------------------------------------------------------------------------------

st.subheader("Age Grouped based in Pakistan")    

# four sliders:
slider1 = st.slider("Childage group", min_value=0, max_value=100, value=50)
slider2 = st.slider("Teenage group", min_value=0, max_value=100, value=50)
slider3 = st.slider("Adultage group", min_value=0, max_value=100, value=50)
slider4 = st.slider("Senior-citizens age group", min_value=0, max_value=100, value=50)

# click button
if st.button("View groups data"):

    groups = ["Childage group", "Teenage group", "Adultage group", "Senior-citizens age group"]
    list = [slider1, slider2, slider3, slider4]

    # Create Pie Chart
    fig, ax = plt.subplots()
    ax.pie(list, labels=groups, autopct="%1.1f%%", colors=["#FFB6C1", "#FFDAB9", "#87CEFA", "#98FB98"])

    # Title
    ax.set_title("Persontage of citizens")

    # Display Graph in Streamlit
    st.pyplot(fig)

#------------------------------------------------------------------------------------------------

st.subheader("Gender wise Population")

#paragraph:
st.write("The gender-wise population distribution provides insights into the demographic structure of a region. Typically, populations are divided into male and female categories, with some countries also recognizing non-binary or other gender identities. In many parts of the world, the male population slightly outnumbers the female population, though this varies based on factors such as birth rates, life expectancy, and migration patterns. Women generally have a higher life expectancy than men, leading to a greater number of females in older age groups. Understanding gender distribution is crucial for policy-making, resource allocation, and planning for healthcare, education, and employment opportunities.")

import streamlit as st
import matplotlib.pyplot as plt

st.header("Gender wise Population Data")

# Creating two columns for horizontal alignment
col1, col2, col3 = st.columns(3)  # Three columns for three genders

with col1:
    male_population = st.number_input("Male Population", min_value=0, step=2, value=500)

with col2:
    female_population = st.number_input("Female Population", min_value=0, step=2, value=400)

with col3:
    other_population = st.number_input("Other Population", min_value=0, step=2, value=50)

# Button to visualize data
if st.button("Visualize Data"):
    st.subheader("Gender Population Bar Graph")

    # Gender names and their respective values
    gender_names = ["Male", "Female", "Other"]
    gender_values = [male_population, female_population, other_population]

    # Creating figure and bar chart
    fig, ax = plt.subplots()
    ax.bar(gender_names, gender_values, color=["pink", "black", "green"])

    ax.set_xlabel("Gender")
    ax.set_ylabel("Population Count")
    ax.set_title("Gender-wise Population Graph")

    st.pyplot(fig)

st.markdown(
    """
    <div style="text-align: center; padding: 10px; font-size: 14px; font-weight: bold; color: #333;">
        Copyrights Reserved &copy; Mueza Ejaz
    </div>
    """,
    unsafe_allow_html=True
)

    



