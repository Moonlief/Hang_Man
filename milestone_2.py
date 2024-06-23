import random

word_list = ["apple","lychee","passion fruit","orange","pineapple"]
word =  random.choice(word_list)

guess = input("please enter a letter ")

print(type(guess))

if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input." )

