from guizero import App, Text, TextBox, PushButton, Slider, Picture

#Funcs
##---------------##
def say_my_name():
    welcome_message.value = my_name.value

def change_text_size(slider_value):
    welcome_message.size = slider_value
##---------------##
app = App(title="Hello world")

#Gui
##---------------##
welcome_message = Text(app, text="Welcome to my app", size=40, font="Times New Roman", color="lightblue")
my_name = TextBox(app)
pdate_text = PushButton(app, command=say_my_name, text="Display my name")
text_size = Slider(app, command=change_text_size, start=10, end=80)
my_cat = Picture(app, image="kitten.jpg")
##---------------##
app.display()
