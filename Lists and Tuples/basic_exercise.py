
# ✅ Exercises on Lists & Tuples:

# 🔹 Basic Level:
# 1️⃣ Ek list fruits banayein jisme "apple", "banana", "cherry" ho aur "banana" ko print karein.

fruits_list = ["apple","banana", "cherry"]
list = fruits_list[1]
print(list) # banana / print(fruits_list[1])
#---------------------------------------------------------------------

# 2️⃣ Ek tuple numbers banayein jisme 10, 20, 30, 40 ho aur 30 ka index print karein.

tuple = (10,20,30,40)
final = tuple.index(30)
print(final) # 2
#---------------------------------------------------------------------

# 3️⃣ Ek list banayein jisme 5 numbers ho aur unka sum aur average calculate karein.

list = [1,2,3,4,5]
sum = sum(list)
average = sum/len(list)
print(sum) # 15
print(average) # 3.0
#----------------------------------------------------------------------

# 4️⃣ Ek tuple banayein aur check karein ke koi specific element usme maujood hai ya nahi.

tuple = (10,20,30,40,20)
final = tuple.count(20)
print(final) # 2
#----------------------------------------------------------------------

# 5️⃣ Ek list banayein aur uske first aur last element ko swap karein.

list = [20,40,70,5,9,3,1]
# replace first element to last element:
list[0],list[6] = list[6],list[0]
#updated list:
print(list) # [1, 40, 70, 5, 9, 3, 20]

