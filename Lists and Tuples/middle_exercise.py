
# 🔹 Intermediate Level:

# 6️⃣ Ek list me duplicate values hoon, usko unique values me convert karein.

my_list = [20, 50, 20, 40, 5, 20, 50, 20]

unique_list = list(set(my_list))
print(unique_list) # [40, 50, 20, 5]
#-------------------------------------------------------------------

# 7️⃣ Ek tuple banayein aur usko reverse karein bina list me convert kiye.
tuple = (1, 2, 3, 4, 5)
new_tuple = tuple[::-1]
print(new_tuple) # (5, 4, 3, 2, 1)
#------------------------------------------------------

# 8️⃣ Do lists ko merge karein aur sorted order me print karein.

list1 = [5,4,3,2,1]
list2 = [6,7,8,9,10]
merge_list = list1 + list2
merge_list.sort()
print(merge_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#-----------------------------------------------------------

# 9️⃣ Ek list me sabse bara aur sabse chhota number find karein.

list = [5,4,3,2,1]
max_num = max(list)
mini_num = min(list)
print("The largest number is", max_num,"\n","The smallest number is", mini_num)# The largest number is 5 and  The smallest number is 1        
#-----------------------------------------------------------------------------------------------

# Ek tuple se ek specific element remove karne ka tariqa
tuple = (1, 2, 3, 4, 5)
element_to_remove = 3
new_tuple = tuple[:tuple.index(element_to_remove)] + tuple[tuple.index(element_to_remove) + 1:]
print(new_tuple) # (1, 2, 4, 5)




