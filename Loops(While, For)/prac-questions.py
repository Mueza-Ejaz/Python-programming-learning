# 1- print numbers from 1 to 1oo.

i = 1
while i<= 100:
    print(i)
    i+= 1 # cmd = 1------100

#----------------------------------------------------------

# 2- print numbers from 100 to 1.

i = 100
while i>= 1:
    print(i)
    i-= 1 # cmd = 100------1

#---------------------------------------------------------------------


# 3- print the multiplication table of a number n.

# Part 1 :

i = 1
while i <= 10:
    print(f" n * {i} = n{i}")
    i+= 1

# cmd:
#  n * 1 = n1
#  n * 2 = n2  
#  n * 3 = n3  
#  n * 4 = n4  
#  n * 5 = n5  
#  n * 6 = n6  
#  n * 7 = n7  
#  n * 8 = n8  
#  n * 9 = n9  
#  n * 10 = n10

# Part 2:

n = int(input("Enter a Number:"))
i = 1
while i <= 10:
    print(f" {n} * {i} = {n*i}")
    i+= 1

#cmd:
# Enter a Number:5
#  5 * 1 = 5
#  5 * 2 = 10
#  5 * 3 = 15
#  5 * 4 = 20
#  5 * 5 = 25
#  5 * 6 = 30
#  5 * 7 = 35
#  5 * 8 = 40
#  5 * 9 = 45
#  5 * 10 = 50    

#---------------------------------------------------------------

# 4- print the elements of the following list using a loop.
    # [1,4,9,16,25,36,49,64,81,100]

numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for num in numbers:
    print(num)

#cmd:
# 1
# 4  
# 9  
# 16 
# 25 
# 36 
# 49 
# 64 
# 81 
# 100

#-------------------------------------------------------------------------------

# 5- search for a number x in this list using loops.
    # [1,4,9,16,25,36,49,64,81,100]

list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = int(input("Enter a number to search: ")) 

found = False  # Initially assume number is not find 
for num in list:
    if num == x:
        found = True
        break  # Number mil gaya to loop exit

if found:
    print(f"{x} is found in the list!")
else:
    print(f"{x} is not in the list!")

