"""
War Card game using Guizero
Corey Fults
"""
from guizero import App, Text, PushButton, Window, Box, Picture
import random
from deck import Deck, Hand
#---Funcs---#
imgDir = "./Images/card-pngs/"
cardBacks = ["red_back","yellow_back","purple_back", "blue_back", "green_back", "gray_back"]

currentDeck = []
leftHand = []
rightHand = []
leftScore = 0
rightScore = 0
acesHigh = False

#--Choose random card back
def random_back():
    return random.choice(cardBacks)

#--Show game window
def show_game():
    reset()
    gameWindow.show()
    appWindow.hide()

#--Show main menu
def show_main():
    gameWindow.hide()
    appWindow.show()

#--Display played cards
def update_hands_ui(lh,rh):
    cardLeft.image = imgDir+lh+".png"
    cardRight.image = imgDir+rh+".png"

#--Reset game to base state
def reset():
    global leftScore, rightScore, leftHand, rightHand
    leftScore = 0
    rightScore = 0
    leftHand = []
    rightHand = []
    playBut.visible = True
    dealBut.visible = False
    update_gui()
    clear_round_win_gui()
    chosenCardBack = random_back()
    update_hands_ui(chosenCardBack, chosenCardBack)


#--Update value tracking guis 
def update_gui():
    global leftHand, rightHand
    leftCardCount.value = len(leftHand.cards) if type(leftHand) == Hand else 0
    rightCardCount.value = len(rightHand.cards) if type(rightHand) == Hand else 0
    leftScoreUI.value = "P1 Score: "+str(leftScore)
    rightScoreUI.value = "P2 Score: "+str(rightScore)

#--Display round winner
def round_win_gui(winner):
    if winner == 0:
        leftWinUI.value = "Round Win +1"
        rightWinUI.value = ""
    elif winner == 1:
        leftWinUI.value = ""
        rightWinUI.value = "Round Win +1"
    else:
        leftWinUI.value = "Draw +.5"
        rightWinUI.value = "Draw +.5"

def clear_round_win_gui():
    leftWinUI.value = ""
    rightWinUI.value = ""        

#--Start a new game
def start_game():
    global acesHigh
    playBut.visible = False
    dealBut.visible = True
    global currentDeck, leftHand, rightHand

    currentDeck = Deck()
    currentDeck.Shuffle()
    players = [Hand(), Hand()]
    currentDeck.Deal(players)

    leftHand = players[0]
    rightHand = players[1]
    update_gui()
    acesHigh = gameWindow.yesno(title="Game Option", text="Aces High?")

#--Display winner and show buttons
def end_game():
    global leftScore, rightScore
    gameWindow.info(title="Game Over!", text="Winner - "+("Player 1" if leftScore > rightScore else ("Player 2" if rightScore > leftScore else "Draw" )))
    reset()
    
    
#--Get value of the card for scoring
def get_card_val(card):
    global acesHigh
    if card.number in ["J", "Q", "K", "A"]:
        if card.number == "A":
             return 14 if acesHigh else 1
        if card.number == "J":
            return 11
        if card.number == "Q":
            return 12
        if card.number == "K":
            return 13
    return int(card.number)

#--Deal the round and update scores
def deal_round():
    global leftHand, rightHand, leftScore, rightScore
    if len(leftHand.cards) == 0 or len(rightHand.cards) == 0:
        return

    p1card = leftHand.Play()
    p2card = rightHand.Play()
    update_hands_ui(str(p1card), str(p2card))
    leftCardCount.value = len(leftHand.cards)
    rightCardCount.value = len(rightHand.cards)

    if get_card_val(p1card) > get_card_val(p2card):
        leftScore += 1
        round_win_gui(0)
    elif get_card_val(p1card) < get_card_val(p2card):
        rightScore += 1
        round_win_gui(1)
    else:
        leftScore+=.5
        rightScore+=.5
        round_win_gui(-1)
        
    update_gui()

    if len(leftHand.cards) == 0 or len(rightHand.cards) == 0:
        end_game()

    
#---Window/App Declaration---#
appWindow = App(title="War Menu", width=300, height=50)

gameWindow = Window(appWindow,  title="War App", width=500, height=600, layout="grid")
gameWindow.hide()
gameWindow.when_closed = show_main

#---Main Window---#
button = PushButton(appWindow, text="Start Game", width="fill",command=show_game)


#---Second Window---#

topBox = Box(gameWindow,width="fill", grid=[0,0])
topBox2 = Box(gameWindow, width=500, height=50, grid=[0, 1], border=True)
midBox = Box(gameWindow, width="fill", grid=[0, 2])
botBox = Box(gameWindow, width=500, height=50, grid=[0, 3], border=True)
botBox2 = Box(gameWindow, width=500, height=50, grid=[0, 4], border=True)

playBut = PushButton(topBox, text="Play", width="fill", command=start_game, align="left")
exitBut = PushButton(topBox, text="Exit", width="fill", command=show_main, align="right")
dealBut = PushButton(topBox, text="Deal", width="fill", command=deal_round, visible=False)

cardLeft = Picture(midBox, image=imgDir+"red_back.png", height=350, width=250, align="left")
cardRight = Picture(midBox, image=imgDir+"red_back.png", height=350, width=250, align="right")

leftCardCount = Text(topBox2, "",  width=25, height=50, align="left")
rightCardCount = Text(topBox2, "",   width=25, height=50, align="left")

leftWinUI = Text(botBox, "",  width=25, height=50, align="left")
rightWinUI = Text(botBox, "",   width=25, height=50, align="left")

leftScoreUI = Text(botBox2, "",  width=25, height=50, align="left")
rightScoreUI = Text(botBox2, "",   width=25, height=50, align="left")



#---END---#
appWindow.display()
