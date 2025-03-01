
# Basic Dictionary Tasks:

# Task 1: Create a Dictionary
# Ek dictionary banao jo kisi bhi 3 logon ke naam aur unke cities store kare.

dict = {

    "Ali" : "Karachi",
    "Laiba" : "Sakhar",
    "Yasir" : "Hyderabad"
}

# Task 2: Add a New Key-Value Pair
# Ek dictionary di gayi hai, isme ek new key-value pair add karo

person = { 
        "name": "Aisha",
        "age": 25
    }

add_new = {"city":"Multan"}
person.update(add_new)
print(person) # {'name': 'Aisha', 'age': 25, 'city': 'Multan'}

# Task 3: Get Value from Dictionary
# Ek dictionary di gayi hai, usme se kisi ek key ka value retrieve karo.

car = {

       "brand": "Toyota", 
       "model": "Corolla", 
       "year": 2022

}

print(car["model"])# Corolla


# Task 4: Check if a Key Exists
# Ek dictionary me check karo ke ek specific key exist karti hai ya nahi.

fruits = {"apple": 5, "banana": 8, "orange": 3}

if "banana" in fruits:
    print("Key Exist")

else:
    print("Key not Exist")




    