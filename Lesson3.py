# Task 1

sentance = input("Please enter the Sentance: ")
word1 = input("Enter the word to replace: ")
word2 = input("enter the new word: ")


print(sentance.replace(word1, word2))


# Task 2

sentance1 = input("Enter the sentance: ")
words = sentance.split()

print(max(words, key=len))


# Task 3

word3 = input("Enter first Word: ").lower()
word4 = input("Enter Second word: ").lower()


print(sorted(word3) == sorted(word4))
