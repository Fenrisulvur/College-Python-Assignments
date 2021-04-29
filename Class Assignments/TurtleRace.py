"""
Turtle Race
This is a program to generate turtles based on an array of colors and make them race.
Corey Fults
"""
from turtle import *
from random import randint

speed(0)
penup()
goto(-140,140)

#Array of turtles
RaceTurtles = []
#Array of colors (Will only work on the first 7) Remove or add colors to increase or decrease race participants up to 7
Colors = ["red","blue","yellow","violet","magenta","turquoise","tomato"]

#Draw race track
def DrawTrack():
    for i in range(15):
        write(i, align="center")
        right(90)
        pendown()
        for step in range(8):
            pendown()
            forward(10)
            penup()
            forward(10)

        backward(160)
        left(90)
        forward(20)

#Create, Place, and Spin turtles. Add to turtle array.
def CreateTurtles():
    dirFlip = False
    for i in range(max(0, min(7, len(Colors)))):
        turtle = Turtle()
        turtle.color(Colors[i])
        turtle.shape('turtle')
        turtle.penup()
        turtle.goto(-160, 20 * i)
        turtle.pendown()
        #Flip direction of spin
        turtle.right(360 * (1 if dirFlip else -1) )
        RaceTurtles.append(turtle)
        dirFlip = not dirFlip

#Run the game
def StartGame():
    DrawTrack()
    CreateTurtles()
    for turn in range(100):
        for turt in RaceTurtles:
            turt.forward(randint(1, 5))

StartGame()

#Prevent instant close from race completion
input("Press any key to close...")