"""
Rock Paper Scissors game
Corey Fults
"""
from random import randint
moves = ["r","p","s"]
score = [0,0]

#Get player input
def get_input():
    while True:
        user_choice = input("Enter your move: (r)Rock (p)Paper (s) Scissors: ").lower()
        if user_choice in moves and len(user_choice) == 1:
            return user_choice
        elif len(user_choice) != 1:
            print("Input must be 1 character.")
        else:
            print("Invalid input.")

#Get computer move
def get_cp_move():
    cp_move = randint(1,3)
    translated_move = moves[cp_move-1]
    return translated_move

#Get input for playing another round
def get_continue():
    while True:
        user_choice = input("Play another round? [y/n]: ").lower()
        if user_choice == "y":
            return True
        elif user_choice == "n":
            return False
        elif len(user_choice) != 1:
            print("Input must be 1 character.")
        else:
            print("Invalid input.")

#Reset scoreboard (Incase I add the ability to play another game)
def reset_score():
    score = [0,0]

#Determine winner
def winner():
    if score[0] > score[1]:
        return "Player"
    elif score[0] < score[1]:
        return "Computer"
    else:
        return "Draw"

#Round logic
def determine_round_outcome(p,cp):
    print("Your move - %s, Computer move - %s"%(p,cp))
    if p == "r" and cp =="s" or p =="p" and cp =="r" or p =="s" and cp =="p":
        print("Player wins the round")
        score[0]+=1
    elif cp == "r" and p =="s" or cp =="p" and p =="r" or cp =="s" and p =="p":
        print("Computer wins the round")
        score[1]+=1
    else:
        print("Stalemate")

#Main game loop 
def game_loop():
    playing = True
    while playing:
        p = get_input()
        cp = get_cp_move()
        determine_round_outcome(p,cp)
        playing = get_continue()

game_loop()
print("Final score: Player - %s, Computer - %s" % (score[0], score[1]))
print("Winner: "+ winner())
reset_score()