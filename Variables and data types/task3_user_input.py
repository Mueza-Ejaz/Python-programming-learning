# User Input and Data Types:

name = input("Enter Your Name:")
age = input("What's your age:")
height = input("Mention your height:")

# Printing Before Conversion:
print("BEFORE CONVERSION:")
print("\nMy good name is:", name, "|", type(name))
print("I am", age, "year's old.", "|", type(age))
print("My height is:", height, "|", type(height))

# Converting age to integer and height to float:
age1 = int(age)
height1 = int(height)

# Printing After Conversion:
print("After CONVERSION:")
print("\nI am", age1, "year's old.", "|", type(age1))
print("My height is:", height1, "|", type(height1))

