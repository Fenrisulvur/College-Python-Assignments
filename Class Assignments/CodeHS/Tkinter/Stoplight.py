"""
Corey Fults.

Assignment:
    You should have a gray rectangle, and then three circles in the rectangle. 
    The circles should be red, then yellow, then green. You should use a draw_circle function.
    The rectangle should be centered on the screen. 
    The yellow light should be centered on the screen, and the red and green light should be offset by the dist_between_lights amount.

"""
from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 400
light_radius = 35
stoplight_width = 120
stoplight_height = 350
dist_between_lights = 120

# Create canvas
screen = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
screen.pack()

# Write your program here!


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
    return screen.create_oval(x0, y0+offset, x1, y1+offset, fill=color)


draw_rectangle(canvas_width/2, canvas_height/2,
               stoplight_width/2, stoplight_height/2, "lightgray")

draw_circle(canvas_width/2, canvas_height/2, light_radius)
draw_circle(canvas_width/2, canvas_height/2,
            light_radius, -dist_between_lights, "red")
draw_circle(canvas_width/2, canvas_height/2,
            light_radius, dist_between_lights, "green")

# Add shapes to canvas
mainloop()
