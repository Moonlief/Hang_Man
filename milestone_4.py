
import random

word_list = ["apple","lychee","passion fruit","orange","pineapple"]
word =  random.choice(word_list)



class Hangman:
    #Constructor
    def __init__(self, word_list, num_lives= 5):
        
        self.word =  random.choice(word_list)

        self.word_guessed = ['_'] * len(self.word)

        self.num_letters = int(len(self.word) -len(set(self.word_guessed)))
        
        self.num_lives = num_lives

        word_list = ["apple","lychee","passion fruit","orange","pineapple"]

        self.list_of_guesses = []

    #Method (method is a function within a class)


    def check_guess(guess):
        lowercase = guess.lower()

        for letter in self.word:

            if letter == guess:
                print(f"Good guess! {guess} is in the word.")
                
                #n the if block, replace the corresponding "_" in the word_guessed with the guess. 
                # HINT: You can index the word_guessed at the position of the letter 
                # and assign it to the letter

                x = self.word.index(guess) #show number
                word_guessed[x] = guess
                


            else:
                num_lives -= 1
                print(f"Sorry, {guess} is not in the word. Try again.")
                print(f""You have {num_lives} lives left.")

        num_letters += 1


    def ask_for_input(guess):
        while True:
            if guess.isalpha() != True or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                check_guess(guess)
                list_of_guesses.append(guess)
                ask_for_input(guess) 

               

        
guess = input("Please guess a letter: ")


