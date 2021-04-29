"""
Corey Fults.

Assignment:
    Write a program to draw multiple ghosts on the screen. 
    You must do this by writing a function called draw_ghost, which takes three parameters, the center x location of the ghost, the center y location of the ghost and the color of the ghost.

"""
# Get the height and width of the canvas
width = get_width()
height = get_height()

# Dimensions of each shape
head_radius = width/6
body_width = head_radius * 2
body_height = height/6
num_feet = 3
foot_radius = body_width / (num_feet * 2)
eye_radius = head_radius/4
eye_offset = eye_radius * 1.5
pupil_radius = eye_radius/2.5
pupil_left_offset = eye_radius
pupil_right_offset = pupil_radius * 5

# Colors (These can be altered!)
eye_color = Color.white
pupil_color = Color.blue


def draw_rectangle(x, y, w, h, color=""):
    x0 = x - w
    y0 = y - h
    x1 = x + w
    y1 = y + h
    rec = Rectangle(w, h)
    rec.set_color(color)
    rec.set_position(x, y)
    add(rec)


def draw_circle(x, y, r, offset=0, color=""):
    circle = Circle(r)
    circle.set_position(x, y)
    circle.set_color(color)
    add(circle)


def draw_ghost(x, y, color):
    draw_rectangle(x-body_width/2, y, body_width, body_height, color)
    draw_circle(x, y, head_radius, -body_height/2, color)

    draw_circle(x, y+body_height, foot_radius,  body_height/2, color)
    draw_circle(x-body_width/num_feet, y+body_height,
                foot_radius,  body_height/2, color)
    draw_circle(x+body_width/num_feet, y+body_height,
                foot_radius,  body_height/2, color)

    draw_circle(x-eye_offset, y, eye_radius,  -body_height/2, eye_color)
    draw_circle(x-pupil_left_offset, y, pupil_radius,  -
                body_height/2, pupil_color)

    draw_circle(x+eye_offset, y, eye_radius,  -body_height/2, eye_color)
    draw_circle(x+pupil_right_offset, y, pupil_radius,  -
                body_height/2, pupil_color)


draw_ghost(200, 200, Color.purple)
draw_ghost(150, 300, Color.orange)
draw_ghost(100, 100, Color.cyan)
draw_ghost(300, 350, "#FE7F9C")
