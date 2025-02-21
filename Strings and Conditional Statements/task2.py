
# Password Strength Checker:

# Ask the user to enter a password;
# - If the password length is less than 6, print "Weak Password".
# - If it contains both letters and numbers and is at least 8 characters long, print "Strong Password".
# - Otherwise, print "Moderate Password".
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

password = input("Enter the strong password:")
length = len(password)
if length < 6: 
    print("Weak Password")
elif length >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
    print("Strong Password")

else:
 print("Moderate Password")
   
     

