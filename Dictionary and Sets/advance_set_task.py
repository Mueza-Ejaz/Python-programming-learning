
# Advanced Level:

# 1- Ek list [1, 2, 2, 3, 4, 4, 5, 6, 6] lo aur ismein se duplicate values hata kar ek set banao.

list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
new_list = set(list)
print(new_list) # {1, 2, 3, 4, 5, 6}


# 2- Do sets {‘a’, ‘b’, ‘c’} aur {‘c’, ‘d’, ‘e’} ka difference find karo.

A = {'a', 'b', 'c'}
B = {'c', 'd', 'e'}
print(A-B) # {'a', 'b'}
# Alternative Method (Using difference() Function)
print(A.difference(B)) # {'b', 'a'}  


# 3- Ek set {10, 20, 30} lo aur pop() function ka use karke koi ek element remove karo.
num_set = {10, 20, 30}
num_set.pop()
print(num_set) # {20, 30}


# 4- Ek set {‘cat’, ‘dog’, ‘rabbit’} banao aur ek naya set {‘dog’, ‘elephant’} ke saath update karo.
animals_set = {'cat', 'dog', 'rabbit'}
animals_set.update({'dog','elephant'})
print(animals_set) # {'cat', 'dog', 'rabbit', 'elephant'}


# 5- Ek dictionary {‘name’: ‘Ali’, ‘age’: 25, ‘city’: ‘Karachi’} lo aur is dictionary ke keys ko ek set mein convert karo.

dict = {
    'name': "Ali",
    'age': 25,
    'city': "Karachi"
}

#dict_keys(['name', 'age', 'city'])
print(set(dict.keys())) # {'city', 'name', 'age'}