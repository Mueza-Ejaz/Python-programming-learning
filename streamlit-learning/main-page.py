import streamlit as za

za.title("webapp") 
za.header("Growth Mind Web App") # Main Heading
za.subheader("Enginer Zain Shah") # sub heading
za.markdown(
    "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."
)

name = za.text_input("What's your good name?")# input field
if name:
    za.write(f"My name is , {name}") # for print

                                             #starting| Ending| default value
age = za.number_input("What's your age?", min_value=18, max_value=100, value=25)
za.write(f"I am {age} year's old.")

value = za.slider("value", min_value=0, max_value=100, value=50)
# za.write(f"value you selected {value}")

if za.button("click me"):
    za.write(f"You have successfully submit this value: {value} ") # button

option = za.radio("Select your favorite color", ("Red", "Blue", "Green"))
za.write(f"You selected {option}")    


uploaded_file = za.file_uploader("Choose a file")
if uploaded_file:
    za.write(f"File uploaded: {uploaded_file.name}")


agree = za.checkbox("I agree to the terms and conditions")
if agree:
    za.write("You agreed!")





# value = st.slider("Select a value", min_value=0, max_value=100, value=50)
# st.write(f"You selected {value}")


# age = st.number_input("Enter your age", min_value=18, max_value=100, value=25)
# st.write(f"Your age is {age}")