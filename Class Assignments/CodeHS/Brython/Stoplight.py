"""
Corey Fults.

Assignment:
    You should have a gray rectangle, and then three circles in the rectangle. 
    The circles should be red, then yellow, then green. You should use a draw_circle function.
    The rectangle should be centered on the screen. 
    The yellow light should be centered on the screen, and the red and green light should be offset by the dist_between_lights amount.

"""


light_radius = 35
box_width = 120
box_height = 350
dist_between_lights = 120


def draw_rectangle(x, y, w, h, color=""):
    x0 = x - w
    y0 = y - h
    x1 = x + w
    y1 = y + h
    rec = Rectangle(w, h)
    rec.set_color(color)
    rec.set_position(x, y)
    add(rec)


def draw_circle(x, y, r, offset=0, color="#ffe100"):
    circle = Circle(r)
    circle.set_position(x, y+offset)
    circle.set_color(color)
    add(circle)


draw_rectangle(get_width()/2-box_width/2, get_height()/2 -
               box_height/2, box_width, box_height, "#b3b3b3")

draw_circle(get_width()/2, get_height()/2, light_radius)
draw_circle(get_width()/2, get_height()/2,
            light_radius, -dist_between_lights, "#ff2a00")
draw_circle(get_width()/2, get_height()/2, light_radius,
            dist_between_lights, "#2fff00")
