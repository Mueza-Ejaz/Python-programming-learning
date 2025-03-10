# Basic Level:

# 1- Ek set banao jisme {1, 2, 3, 4, 5} elements hon. Phir check karo ke 3 is set mein hai ya nahi.

numSet = set([1, 2, 3, 4, 5])

if 3 in numSet:
    print("Exist")
else:
    print("Not Exist")


# 2- Do sets {1, 2, 3} aur {3, 4, 5} ka union aur intersection nikal kar print karo.

a = {1, 2, 3}
b = {3, 4, 5}
print(a|b) # method one
print(a.union(b)) # method two # {1, 2, 3, 4, 5}
print(a & b) # / print(a.intersection(b)) # {3}

# 3- Ek empty set banao aur usmein apple, banana, aur cherry add karo.

emptySet = set([])
emptySet.update(["apple", "banana", "cheery"])
print(emptySet) # {'banana', 'apple', 'cheery'}


# 4- Ek set {10, 20, 30, 40} lo aur ismein 50 add karo.

newSet = {10, 20, 30, 40}
newSet.add(50)
print(newSet) # {40, 10, 50, 20, 30}


# 5- Ek set {1, 2, 3, 4, 5} lo aur 3 ko remove karo.

newSet = {1, 2, 3, 4, 5}
newSet.remove(3)
print(newSet)






