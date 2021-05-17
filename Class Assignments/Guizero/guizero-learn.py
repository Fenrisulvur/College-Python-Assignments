from guizero import App, Text, PushButton, Window, Box, TextBox
#---Funcs---#
def say_goodbye(first_name, last_name):
    text.value = first_name + " " + last_name

def open_window():
    window.show(wait=True)

def close_window():
    window.hide()

#---Window/App Declaration---#
app = App(title="Main window")
window = Window(app,  title="Second window")
window.hide()
app.info("info", "this is a guizero app")

#---Main Window---#
message = Text(app, text="Welcome to the Hello world app!")
text = Text(app)
text.text_color = (0, 255, 0)
button = PushButton(app, command=say_goodbye, args=['John', 'Doe'])
open_button = PushButton(app, text="Open", command=open_window)


#---Second Window---#
title_box = Box(window, width="fill", align="top", border=True)
Text(title_box, text="title")

buttons_box = Box(window, width="fill", align="bottom", border=True)
Text(buttons_box, text="buttons")

options_box = Box(window, height="fill", align="right", border=True)
Text(options_box, text="options")

content_box = Box(window, align="top", width="fill", border=True)
Text(content_box, text="content")

form_box = Box(content_box, layout="grid", width="fill", align="left", border=True)
Text(form_box, grid=[0, 0], text="form", align="right")
Text(form_box, grid=[0, 1], text="label", align="left")
TextBox(form_box, grid=[1, 1], text="data", width="fill")

close_button = PushButton(buttons_box, grid=[0, 1], text="Close", command=close_window)


#---END---#
app.display()
