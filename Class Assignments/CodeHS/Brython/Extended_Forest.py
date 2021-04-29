"""
Corey Fults.

Assignment:
    Expand the Forest example found in a previous lesson.

    First, add leaves to the trees using circles. Use a function and any control structures to make your program more concise and easier to follow.

    Next, allow the user to enter the information required to add trees. Ask the user how many trees they want to add and then ask for the x-coordinate and height for each tree.

    Then, allow the trees to always fit on the screen. If the user enters an x or y value that is off-screen, have them enter a new value.

    Finally, get creative! Add anything you think will bring more joy to your forest. Additional options include:
    Add some animals
    Add a sun or clouds in the sky
    Add a house or cabin in the forest
"""

import random
from browser import timer
# Get the height and width of the canvas
canvas_width = get_width()
canvas_height = get_height()

# Dimensions for shapes
trunk_width = canvas_width/20
leaves_width = trunk_width * 4
leaves_height = leaves_width * 2

#colors for leaves
leaf_colors = ["#FF9900", "#3A5F0B", "#FFCC00"]

#landscape
sky = Rectangle(canvas_width, canvas_height)
sky.set_position(0, 0)
sky.set_color("#87ceeb")
add(sky)
ground = Rectangle(canvas_width, canvas_height)
ground.set_position(0, canvas_height-10)
ground.set_color("#136d15")
add(ground)
sun = Circle(20)
sun.set_position(canvas_width - 30, 30)
sun.set_color("#F9D71C")
add(sun)

# This function draws a tree at a given location


def draw_tree(x, height):
    trunk = Rectangle(trunk_width, height - leaves_height)
    trunk.set_position(x - trunk_width/2, canvas_height -
                       height + leaves_height)
    trunk.set_color("#3F301D")
    add(trunk)
    leaves = Rectangle(leaves_width, leaves_height)
    leaves.set_position(x - leaves_width/2, canvas_height - height)
    leaves.set_color(Color.green)
    add(leaves)
    leaf_color_pallete = random.choice(leaf_colors)
    for i in range(random.randint(8, 70)):
        leaves_small = Circle(5)
        leaves_small.set_position(x + random.randint(-leaves_width//2+5, +leaves_width//2-5), canvas_height -
                                  height + leaves_height/2 + random.randint(-leaves_height//2+5, +leaves_height//2-5))
        leaves_small.set_color(leaf_color_pallete)
        add(leaves_small)


#verification of tree inside screen bounds
def verify_inbounds(coord, debug=False):
    if debug:
        print("Testing: ", coord)
    x_test = coord[0] + max(leaves_width, trunk_width)/2
    x_test_2 = coord[0] - max(leaves_width, trunk_width)/2

    if debug:
        print(" X test", x_test, x_test_2)

    if x_test > canvas_width or x_test_2 < 0:
        print("     ", coord, "Is out of range in x axis")
        return False

    y_test = canvas_height - coord[1] + leaves_height
    y_test_2 = canvas_height - coord[1]

    if debug:
        print(" Y test", y_test, y_test_2)

    if y_test > canvas_height or y_test_2 < 0:
        print("     ", coord, "Is out of range in y axis")
        return False

    return True

#grab user number input within set bounds


def get_user_input_num(text, min, max):
    while True:
        user_inp = ""
        try:
            user_inp = input(text)
            amnt = int(user_inp)
            if len(str(amnt)) == 0 or amnt > max or amnt < min:
                print("Must be a number & between %i-%i" % (min, max))
            else:
                return amnt
        except ValueError:
            if user_inp == "exit":
                raise SystemExit(0)
            print("Must be a number")


#verify_inbounds unit test
def verification_unit_test():
    coordinates = [[40, 200], [360, 350], [190, 160], [250, 480], [200, 490]]
    print("/-/"*20)
    print("Testing coords: ", coordinates)
    print("___"*20)
    print(get_height())
    for coord in coordinates:
        if verify_inbounds((coord[0], coord[1]), True):
            draw_tree(coord[0], coord[1])

    print("/-/"*20)

#Start script


def start():
    tip = "[type exit to force quit at any stage]\n"
    tree_count = get_user_input_num(
        tip+"How many trees do you want?(1-20):", 1, 20)

    for i in range(tree_count):
        x_inp, h_inp = 0, 0
        valid = False
        first_pass = True
        msg_prefix = ""
        while first_pass or not valid:
            msg_prefix = "Tree out of bounds, try again\n" if not first_pass else ""
            first_pass = False
            x_inp = get_user_input_num(
                tip+msg_prefix+"Enter tree %i x pos(%i-%i):" % (i+1, 0, canvas_width), 0, canvas_width)
            h_inp = get_user_input_num(
                tip+msg_prefix+"Enter tree %i height(%i-%i):" % (i+1, 0, canvas_height), 0, canvas_height)
            # <===== Overload this with True as an addition parameter to see debug output for the inbounds test
            valid = verify_inbounds((x_inp, h_inp))
            if not valid:
                print("Tree is not within screen bounds, try again.")
        draw_tree(x_inp, h_inp)


"""

Uncomment the verification test below to test the code without user input (makes it faster to test).
If you do use the verification test, comment out start so it doesnt interfere.
If you get stuck in the input box, type exit to force shutdown. This module on CodeHS uses javascript style input instead of console style;
this makes it 100x more annoying so I implemented a force quit.
"""

#verification_unit_test()
start()

"""
draw_tree(50, 200)
draw_tree(250, 400)
draw_tree(350, 350)
"""
