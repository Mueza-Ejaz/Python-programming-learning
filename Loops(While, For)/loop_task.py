# Task 1: While Loop - Countdown Timer

# Write a program that takes a number as input and uses a while loop to count down from that number to 0. At each step, it should print the current number. When the countdown reaches 0, it should print "Blast off!".

num = int(input("Enter a number:"))  

while num>=0:
    if num == 0:
        print("Blast off!")
        break
    print(num) 
    num -= 1

# Answer: 
# Enter a number:5
# 5
# 4
# 3
# 2
# 1
# Blast off!
#----------------------------------------------------------------------------- 

# Task 2: For Loop with Range - Sum of Even Numbers

# Write a program that calculates the sum of even numbers from 1 to 100 using a for loop and the range function.
# Hint: Use range(start, stop, step) to iterate over even numbers directly.

EvenNumb = range(0, 101, 2)  
total_sum = 0
for num in EvenNumb:
    total_sum += num
print(f"Sum of even numbers from 1 to 100 is = {total_sum}")

# Answer:
# Sum of even numbers from 1 to 100 is = 2550
#----------------------------------------------------------------------------------------

# Task 3: For Loop with Range - Multiplication Table
#Write a program that takes a number as input from the user and prints its multiplication table up to 10 using a for loop and the range function.

user_num = int(input("Enter a number:"))
num = range(1,11)

for el in num:
    print(f"{user_num} * {el} = {user_num * el}")

# Answer:
# Enter a number:7 | Enter a number:5

# 7 * 1 = 7   |  5 * 1 = 5  
# 7 * 2 = 14  |  5 * 2 = 10 
# 7 * 3 = 21  |  5 * 3 = 15 
# 7 * 4 = 28  |  5 * 4 = 20 
# 7 * 5 = 35  |  5 * 5 = 25  
# 7 * 6 = 42  |  5 * 6 = 30 
# 7 * 7 = 49  |  5 * 7 = 35
# 7 * 8 = 56  |  5 * 8 = 40  
# 7 * 9 = 63  |  5 * 9 = 45 
# 7 * 10 = 70 |  5 * 10 = 50

#--------------------------------------------------------------------------------------------

# Task 4: Pass Statement - To be Implemented Later
# Write a function that takes a number as input and checks whether it is positive, negative, or zero.

# - If the number is positive, print "Positive Number".
# - If the number is negative, print "Negative Number".
# - If the number is zero, use the pass statement (i.e., do nothing).
# Hint: Use the pass statement only in the case of zero.

user_num = int(input("Enter a number:"))

if user_num > 0:
    print("Postive Number")

elif user_num < 0:
    print("Negative Number")

elif user_num == 0:
    print("No output")
    pass

