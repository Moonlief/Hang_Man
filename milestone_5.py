
import random

word_list = ["apple"]
#,"lychee","passion fruit","orange","pineapple"
word =  random.choice(word_list)


class Hangman:
    #Constructor
    def __init__(self, word_list, num_lives= 5):
        
        self.word =  random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    #Method 


    def check_guess(self, guess):
        ''' check_guess methos is used to see the guess (one letter) matches with any letters in the word'''
        
        lowercase = guess.lower()

        if guess in self.word:
                print(f"Good guess! {guess} is in the word")
                
                for i in range(len(self.word)):
                    if self.word[i] == guess:
                        self.word_guessed[i] = guess
                print(f"Remaining letters:{self.num_letters}. So far the word is: {self.word_guessed}")

                self.num_letters -= 1


                
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
            print(f"Remaining letters:{self.num_letters} Don't Give Up!")


    def ask_for_input(self):
        '''this methods checks the validity of the input of the player. The guess has to be one letter'''
        
        guess = input("Please guess a letter: ")
            
        if guess.isalpha() != True or len(guess) != 1:
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)
            print(self.list_of_guesses)
            

               

        
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list,num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0: 
            game.ask_for_input()
            #why is this game and not Hangman?
        else:
            print("Congratulations! You won the game!")
            break


play_game(word_list)


            


