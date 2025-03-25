# 📝 Part 1: Functions Tasks (Basic to Intermediate)


# Task 1: Greeting Function
# 🔹 Write a function greet(name) that takes a name as input and prints a greeting message.

def greet(name):
    message = f"Hello, {name}! Welcome to Python."
    return message

output = greet("Mueza")
print(output) # cmd: Hello, Mueza! Welcome to Python.
#-------------------------------------------------------------------


# Task 2: Sum of Two Numbers
# 🔹 Create a function add(a, b) that takes two numbers and returns their sum.

def add(a,b):
    sum = a+b
    print(sum)
    return sum

add(5, 10) # cmd 15
#--------------------------------------------------------------------


# Task 3: Check Even or Odd
# 🔹 Write a function check_even_odd(n) that prints whether a number is even or odd.

num = int(input("Enter a number:"))
def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is a even number")
    else:
        print(f"{num} is a odd number") 

check_even_odd(num) # cmd:4 is a even number| 5 is a odd number
#-------------------------------------------------------------------------------


# Task 4: Find the Largest Number
# 🔹 Write a function find_max(a, b, c) that returns the largest number among three inputs.

def find_max(a, b, c):
    if a >= b and a >= c:  # Check if 'a' is the largest
        print(f"The largest number is {a}")
    elif b >= a and b >= c:  # Check if 'b' is the largest
        print(f"The largest number is {b}")
    else:  # If 'a' and 'b' are not the largest, 'c' must be the largest
        print(f"The largest number is {c}")

# Example usage
find_max(10, 25, 7)  # Output: The largest number is 25
find_max(50, 20, 50) # Output: The largest number is 50
#----------------------------------------------------------------------------

# Task 5: Factorial Using Function (Without Recursion)
# 🔹 Write a function factorial(n) that retunrns the factorial of a number using a loop.

num = int(input("Enter a number: "))
def factorial(num):
    result = 1  # Start with 1 (because multiplying by 0 gives 0)
    for i in range(1, num + 1):  # Loop from 1 to n
        result *= i  # Multiply result by i
    return result  # Return the final factorial value


print(f"Factorial of {num} is {factorial(num)}") # Output:Factorial of 5 is 120