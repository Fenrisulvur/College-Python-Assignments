"""
Corey Fults.

Assignment:
    Create a program that asks a user how many blocks should be on the bottom row of the tower (1-20) and then draw a tower that stacks blocks on top of one another, with one less on every higher row.
"""
from tkinter import *

root = Tk()

# Constant values
canvas_width = 400
canvas_height = 400
block_size = 20
blocks = 1

# Create canvas
screen = Canvas(root, width=canvas_width, height=canvas_height)
screen.pack()

##clines for center alignment
screen.create_line(canvas_width/2, 0, canvas_width/2, canvas_height)
screen.create_line(0, canvas_height/2, canvas_width, canvas_height/2)


def draw_pyramid(width, height, num_rows, block_width, block_height):
    for row in range(num_rows):
        base_x = row * block_width // 2
        y = height - (row+.5) * block_height
        print("row", row, "y: ", y, "x: ", base_x,)
        for block in range(num_rows - row):
            x = (width/2 - ((num_rows - row-1) * block_width//2)) + \
                (block_width * block)
            print("     block:", block, "x: ", x,)
            screen.create_rectangle(x-block_width/2, y-block_width/2, x +
                                    block_width/2, y+block_width/2, outline="black", fill="red")


while True:
    try:
        blocks = int(input("How many blocks on the bottom? (1-20): "))
        if len(str(blocks)) == 0 or blocks > 20 or blocks <= 0:
            print("Must be a number & between 1-20")
        else:
            break
    except ValueError:
        print("Must be a number")


draw_pyramid(canvas_width, canvas_height, blocks, block_size, block_size)
mainloop()
