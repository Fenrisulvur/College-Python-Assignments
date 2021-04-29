"""
Corey Fults.

Assignment:
    Word guessing game.
    Have the user enter a character and check if it is in the word.
    10 guesses, -1 guess for every incorrect character guess.
"""

import random

#Vars
words = ["monkey", "applebutter", "orange", "beans"]
secret_word = random.choice(words)
dashes = "-" * len(secret_word)
guesses_left = 10

#repeatedly ask for user guess until correct input is given


def get_guess():
    while True:
        user_input = input("Enter a guess: ")
        if (len(user_input) != 1):
            print("Guess must be exactly one character!")
        elif (str.isdigit(user_input) or user_input.isupper()):
            print("Guess must be a lowercase letter!")
        else:
            return user_input


def update_dashes(word, dashes, guess):
    for w_ind in range(len(word)):
        if word[w_ind] == guess:
            dashes = dashes[:w_ind] + guess + dashes[w_ind+1:]
    return dashes


#Ask for 10 guesses
while guesses_left > 0 and dashes != secret_word:
    print(dashes)
    print("You have %s incorrect guesses remaining" % str(guesses_left))

    guess = get_guess()
    dashes = update_dashes(secret_word, dashes, guess)
    if guess in secret_word:
        print("That letter is in the secret word!")
    else:
        print("That letter is not in the secret word!")
        guesses_left -= 1

#Determine outcome
if guesses_left == 0:
    print("You lose. The word was: %s" % secret_word)
else:
    print("Congrats! You win. The word was: %s" % secret_word)
