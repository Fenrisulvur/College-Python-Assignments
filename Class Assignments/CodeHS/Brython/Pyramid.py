"""
Corey Fults.

Assignment:
    Create a program that asks a user how many rows there should be in the tower. Based on the user’s value (1-8), draw that many rows on the canvas in a pyramid style. 
    Each row should be row_height pixels tall and the top row should be individual_block_width pixels wide. 
    Each row should be individual_block_width pixels larger than the one above it. 
    Each row should be centered around the vertical axis and the bottom row should be situated on the bottom on the canvas.
"""
set_size(400, 400)

# Constant values
canvas_width = get_width()
canvas_height = get_height()
row_height = 50
individual_block_width = 50
amnt = 0
maxblocks = min(canvas_width/individual_block_width, canvas_height/row_height)

# Write your program here

##clines for center alignment


def draw_pyramid(width, height, num_rows, block_width, block_height):
    for row in range(num_rows):
        base_x = row * block_width // 2
        y = height - (row+1) * block_height
        print("row", row, "y: ", y, "x: ", base_x,)
        for block in range(num_rows - row):
            x = (width/2 - ((num_rows - row-1) * block_width//2)) + \
                (block_width * block)
            print("     block:", block, "x: ", x,)
            rec = Rectangle(block_width, block_height)
            rec.set_position(x-block_width/2, y)
            add(rec)


while True:
    try:
        amnt = int(input("How many blocks on the bottom? (1-%i): " % maxblocks))

        if len(str(amnt)) == 0 or amnt > maxblocks or amnt <= 0:
            print("Must be a number & between 1-%i" % maxblocks)
        else:
            break

    except ValueError:
        print("Must be a number")


draw_pyramid(canvas_width, canvas_height, amnt,
             individual_block_width, row_height)
