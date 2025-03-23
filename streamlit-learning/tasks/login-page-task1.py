
# - login page,heading(practice portal)
# - 2 input fields
# - select your age
# - select gender(male,female and other)
# - upload your profile pic.
# - paragraph terms and conditions 
# - check box(i agree with conditions)
# - submit button(if click user created with this username having age and gender is.)


import streamlit as log

log.set_page_config(
    page_title="My Streamlit App", 
    page_icon="🌟",  # This sets a small favicon icon (optional)
    layout="centered"    # Options: "centered" (default) or "wide"
)

log.header("Practice Portal")
name = log.text_input("Enter your name")
passowrd = log.text_input("Enter your password")

age = log.number_input("Select your age", min_value=20, max_value=60, value=23)
gender = log.radio("Choose your gender",  ("Male", "Female", "Other"))
upload_pic = log.file_uploader("Upload your profile pic")

log.markdown(
    "A Terms and Conditions agreement acts as a legal contract between you (the company) and the user. It's where you maintain your rights to exclude users from your app in the event that they abuse your website/app, set out the rules for using your service and note other important details and disclaimers."
)

agree = log.checkbox("I agree with terms and conditions")

if log.button("Submit"):
    log.write(f"User name is {name}")
    log.write(f"User age is {age}")
    log.write(f"User gerder is {gender}")

