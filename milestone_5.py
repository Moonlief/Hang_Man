
import random

word_list = ["apple","lychee","passion fruit","orange","pineapple"]
word =  random.choice(word_list)


class Hangman:
    #Constructor
    def __init__(self, word_list, num_lives= 5):
        
        self.word =  random.choice(word_list)

        self.word_guessed = ['_'] * len(self.word)

        self.num_letters = int(len(self.word) -len((self.word_guessed)))
        
        self.num_lives = num_lives

        word_list = ["apple","lychee","passion fruit","orange","pineapple"]

        self.list_of_guesses = []

    #Method 


    def check_guess(self, guess):
        ''' check_guess methos is used to see the guess (one letter) matches with any letters in the word'''
        lowercase = self.guess.lower()

        for letter in self.word:

            if letter == self.guess:
                print(f"Good guess! {self.guess} is in the word.")

                letter_position = self.word.index(guess)
                self.word_guessed[letter_position] = guess
                
            else:
                self.num_lives -= 1
                print(f"Sorry, {self.guess} is not in the word. Try again.")
                print(f"You have {self.num_lives} lives left.")

        self.num_letters += 1


    def ask_for_input(self, guess):
        '''this methods checks the validity of the input of the player. The guess has to be one letter'''
        self.guess = input("Please guess a letter: ")
        
        while True:
            if guess.isalpha() != True or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                Hangman.check_guess(self.guess)
                Hangman.list_of_guesses.append(self.guess)
                Hangman.ask_for_input(guess) 

                #why does the class need to be mentioned when you want to call the method?

               

        
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list,num_lives)

    while True:
        if num_lives == 0:
            print("You lost!")
        elif game.num_letters >= 0: 
            game.ask_for_input()

            #why is this game and not Hangman?
        else:
            print("Congratulations! You won the game!")

            break

            #File "/Users/student/AICORE/Hang_man/milestone_5.py", line 78, in <module> 
            # play_game(word_list)
            # File "/Users/student/AICORE/Hang_man/milestone_5.py", line 72, in play_game
            # elif Hangman.num_letters > 0:
            #AttributeError: type object 'Hangman' has no attribute 'num_letters'


play_game(word_list)


            


