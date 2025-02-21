# Find the Largest Word:

# -Take a sentence as input from the user and find the longest word in the sentence.

# -Try these tasks, and let me know if you need any help! 
# ---------------------------------------------------------------------------------------------

seten = input("write the senetence:")
longestword = max(seten.split(), key=len)
print(f"The longest word in the sentence is: {longestword}")

