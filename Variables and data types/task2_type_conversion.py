
# Task 2: Type Conversion (Casting)

# Integer to Float:

num = 25 
print("Before:", num, "|", type(num)) # Before: 25 | <class 'int'>
num1 = float(25) 
print("After:", num1, "|", type(num1)) # After: 25.0 | <class 'float'> 

# String to Integer:

str = "456"
print("Before:", str, "|", type(str)) # Before: 456 | <class 'str'>
str1 = int(str)
print("After:", str1, "|", type(str1)) #  After: 456 | <class 'int'>

# Float to Integer:

dec_num = 45.8
print("Before:", dec_num, "|", type(dec_num)) # Before: 45.8 | <class 'float'>
dec_num1 = int(dec_num)
print("After:", dec_num1, "|", type(dec_num1)) # After: 45 | <class 'int'> 
