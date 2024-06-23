




word = "apple"



def check_guess(guess):
    lowercase = guess.lower()

    while True:
        if guess.isalpha() == True and len(guess) == 1:
            break
        else:
            guess = input("Invalid letter. Please, enter a single alphabetical character.")




def ask_for_input(guess):
     for letter in word:
        if letter == guess:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")

guess = input("Please guess a letter: ")
check_guess(guess)
ask_for_input(guess)