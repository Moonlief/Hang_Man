
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

    #Method 


    def check_guess(guess):
        ''' check_guess methos is used to see the guess (one letter) matches with any letters in the word'''
        lowercase = guess.lower()

        for letter in self.word:

            if letter == guess:
                print(f"Good guess! {guess} is in the word.")

                letter_position = self.word.index(guess)
                self.word_guessed[letter_position] = guess
                


            else:
                num_lives -= 1
                print(f"Sorry, {guess} is not in the word. Try again.")
                print(f"You have {num_lives} lives left.")

        num_letters += 1


    def ask_for_input(guess):
        '''this methods checks the validity of the input of the player. The guess has to be one letter'''
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


