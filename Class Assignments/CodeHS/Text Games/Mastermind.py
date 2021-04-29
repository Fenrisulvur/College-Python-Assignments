"""
Corey Fults.

Assignment:
    A 4 digit numerical code will be generated.
    You must guess this code, you will receive hints by the codes RED, WHITE, BLACK.
    RED == Correct Digit in the correct spot. WHITE == Correct Digit in the wrong spot, BLACK = Incorrect digit.
    The hints will be shuffled to make it harder.
"""

import random

# Get user guess


def get_guess():
    while True:
        guess = input("Provide four unique numbers: ")
        passed = True
        duplicate = False
        if len(guess) == 4:
            duplicate = guess[0] == guess[1] or guess[0] == guess[2] or guess[0] == guess[
                3] or guess[1] == guess[2] or guess[1] == guess[3] or guess[2] == guess[3]
        try:
            try:
                for i in range(4):
                    if int(guess[i]) >= 8 or int(guess[i]) <= 0 and len(guess) == 4:
                        passed = False
                        print "You can only use numbers 1-7 as guesses dd"
                if len(guess) != 4:
                    passed = False
                    print "Your guess must consist of 4 numbers!"
                if duplicate:
                    passed = False
                    print "You can only use each number once!"
            except ValueError:
                passed = False
                print "You can only use numbers 1-7 as guesses"
        except IndexError:
            passed = False
            print "You can only use numbers 1-7 as guesses"
        if passed:
            break
    return guess

# Check guess against the code


def check_values(computer_list, user_list):
    response_list = [''] * 4
    for i in range(4):
        if int(user_list[i]) in computer_list:
            if int(user_list[i]) == computer_list[i]:
                response_list[i] = "RED"
            else:
                response_list[i] = "WHITE"
        else:
            response_list[i] = "BLACK"
    random.shuffle(response_list)
    print(response_list)
    return response_list

# Check win condition


def check_win(response_list):
    if response_list == ["RED"]*4:
        return True
    return False

# Generate computer code


def create_comp_list():
    list = []
    for i in range(4):
        temp = random.randint(1, 7)
        while temp in list:
            temp = random.randint(1, 7)
        list.append(temp)

    return list

# Game loop


def play_game():
    computer_list = create_comp_list()
    for i in range(5):
        print("Guesses left: %i" % (5-i))
        user_list = get_guess()
        #Uncomment these to check the code
        #print(computer_list)
        #print(user_list)
        if check_win(check_values(computer_list, user_list)):
            print("Congrats! You've won the game!")
            break
        elif (4-i) == 0:
            print("Sorry! You've lost the game!")
            break

# Print directions


def print_directions():
    print "_"*40
    print("Welcome to Mastermind!")
    print("A 4 digit numerical code will be generated.")
    print("You must guess this code, you will receive hints by the codes RED, WHITE, BLACK.")
    print("RED == Correct Digit in the correct spot. WHITE == Correct Digit in the wrong spot, BLACK = Incorrect digit.")
    print("The hints will be shuffled to make it harder.")
    print("Enjoy!")
    print "_"*40

# Print directions telling the user how to play the game. Then call the
# play_game function to begin the game, using all of your prewritten functions.


print_directions()
play_game()
