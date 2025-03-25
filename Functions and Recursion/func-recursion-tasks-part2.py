# 🌀 Part 2: Recursion Tasks (Intermediate to Advanced)


# Task 1: Factorial Using Recursion
# 🔹 Write a recursive function factorial_recursive(n) that calculates the factorial of n.

def factorial_recursive(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial_recursive(n - 1)  # Recursive case
factorial_recursive(5)
#-----------------------------------------------------------------------------



# Task 2: Countdown Timer
# 🔹 Write a recursive function countdown(n) that prints numbers from n to 1, then prints "Time's up!".

def countdown(n):
    if n == 0: # Base case
       print("Time's up!")  
    else:
        print(n)
        countdown(n - 1) # Recursive case

countdown(5) 
# output : 5
# 4
# 3
# 2
# 1
# Time's up!   

#-----------------------------------------------------------------------------------


# Task 3: Reverse a String Using Recursion
# 🔹 Create a recursive function reverse_string(s) that returns the reverse of a string.

def reverse_string(s):
    if s == "":
        return s
    else:
        return s[-1] + reverse_string(s[:-1])  # Akhri letter + baaki ka reverse 

print(reverse_string("mueza")) # output: azeum

