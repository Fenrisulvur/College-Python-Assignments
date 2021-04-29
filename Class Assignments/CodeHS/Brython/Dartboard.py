"""
Corey Fults.

Assignment:
    Write a program that will draw circles on the canvas until the radius of the circle is 0.

    Circles should be placed from the center and should start with the largest circle that touches all sides of the canvas. 
    The radius should decrease by 25 pixels with each circle. If the circle’s radius is divisible by 50, it should be red. 
    If it is not, it should be yellow.
"""
set_size(400, 400)

radius = 200
flop = True


def draw_circle(x, y, r, offset=0, color=""):
    circle = Circle(r)
    circle.set_position(x, y)
    circle.set_color(color)
    add(circle)


for i in range(0, radius, 20):
    draw_circle(get_width()/2, get_height()/2, radius-i, offset=0,
                color=("#ff0505" if flop else "#ffda05"))
    flop = not flop
