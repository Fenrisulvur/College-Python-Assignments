"""
Corey Fults.

Assignment:
    Write a program to draw multiple ghosts on the screen. 
    You must do this by writing a function called draw_ghost, which takes three parameters, the center x location of the ghost, the center y location of the ghost and the color of the ghost.
"""
from tkinter import *

root = Tk()

# Constant values
canvas_width = 400
canvas_height = 400

head_radius = 70
body_width = head_radius * 2
body_height = 120
num_feet = 3
foot_radius = body_width / (num_feet * 2)

pupil_radius = 8
pupil_left_offset = 16
pupil_right_offset = 40
eye_radius = 20
eye_offset = 28
eye_color = "white"
pupil_color = "blue"

# Create canvas
screen = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
screen.pack()

# Write program here


def draw_rectangle(x, y, w, h, color="yellow"):
    x0 = x - w
    y0 = y - h
    x1 = x + w
    y1 = y + h
    return screen.create_rectangle(x0, y0, x1, y1, outline="", fill=color)


def draw_circle(x, y, r, offset=0, color="yellow"):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return screen.create_oval(x0, y0+offset, x1, y1+offset, outline="", fill=color)


def draw_ghost(x, y, color):
    draw_rectangle(x, y, body_width/2, body_height/2, color)
    draw_circle(x, y, head_radius, -body_height/2, color)

    draw_circle(x, y, foot_radius,  body_height/2, color)
    draw_circle(x-body_width/num_feet, y, foot_radius,  body_height/2, color)
    draw_circle(x+body_width/num_feet, y, foot_radius,  body_height/2, color)

    draw_circle(x-eye_offset, y, eye_radius,  -body_height/2, eye_color)
    draw_circle(x-pupil_left_offset, y, pupil_radius,  -
                body_height/2, pupil_color)

    draw_circle(x+eye_offset, y, eye_radius,  -body_height/2, eye_color)
    draw_circle(x+pupil_right_offset, y, pupil_radius,  -
                body_height/2, pupil_color)


draw_ghost(200, 100, "red")
draw_ghost(100, 200, "green")
draw_ghost(350, 150, "yellow")

# Add shapes to canvas
mainloop()
