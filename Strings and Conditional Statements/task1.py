# Check Vowel or Consonant:
# Write a Python program that takes a single letter as input and checks whether it is a vowel (a, e, i, o, u) or a consonant.


letter = input("Enter the Single letter:").lower()
vowels = ["a", "e", "i", "o", "u"]

if letter in vowels:
    print("This letter is a vowel")
else:
    print("This letter is a consonant")   

