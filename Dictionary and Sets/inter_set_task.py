
# Intermediate Level:

# 1- Do sets {1, 2, 3, 4, 5} aur {4, 5, 6, 7, 8} ka symmetric difference find karo.
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a ^ b) # {1, 2, 3, 6, 7, 8}


# 2- Ek set {‘red’, ‘blue’, ‘green’} lo aur check karo ke ‘yellow’ ismein hai ya nahi.

checkingSet = {'red', 'blue', 'green'}
is_yellow_exist = 'yellow' in checkingSet
print(is_yellow_exist) # False


# 3- Set {‘apple’, ‘banana’, ‘cherry’} ko list mein convert karo.

fruits = {'apple', 'banana', 'cherry'}
fruits_list = list(fruits)  # Convert set to list

# A.issubset(B) check karega ke kya A ke saare elements B me mojood hain ya nahi.
# Kyunki {1, 2, 3} waqai {1, 2, 3, 4, 5} ka subset hai, output True aayega.

print(fruits_list) #  ['banana', 'apple', 'cherry']



# 4- Do sets {1, 2, 3} aur {1, 2, 3, 4, 5} ke beech subset relationship check karo.

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
print(A.issubset(B)) # True


# 5- Ek set {10, 20, 30, 40, 50} lo aur ismein se saare elements remove karo.

remove_elements = {10, 20, 30, 40, 50} 
remove_elements.clear()
print(remove_elements) # set()
