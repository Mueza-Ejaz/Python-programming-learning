
# Word Counter
# Ask the user to enter a sentence. Count how many words are in the sentence and print the result.

sentence = input("Write the one sentence:")
words = sentence.split()
print(f"This sentence contains {len(words)} words")

