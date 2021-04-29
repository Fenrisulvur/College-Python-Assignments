"""
Corey Fults.

Assignment:
    This program will continue to draw circles to the screen until the radius
    of the circle reaches the height of the canvas.
"""

from tkinter import *

root = Tk()

canvas_height = 300
canvas_width = 300
radius = 20

# Create canvas
screen = Canvas(root, width=canvas_width, height=canvas_height)
screen.pack()

# Your code here...


def draw_circle(x, y, r, offset=0, color="yellow"):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return screen.create_oval(x0, y0+offset, x1, y1+offset, outline="black", fill=color)


for i in range(radius, canvas_height+radius, 20):
    draw_circle(i/2, i/2, i/2,  0, "")


mainloop()
