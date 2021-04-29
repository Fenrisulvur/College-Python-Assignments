"""
Barebones auto class launcher for zoom
Corey Fults
"""

import webbrowser
import time 
import datetime
import tkinter as tk
root = tk.Tk()


#Classname, Class time, Days of week to launch, Zoom link to open
classes = [
    ["Python", "07:50:00", [0,1,2,3,4], "https://southhills.zoom.us/j/92936144602?pwd=QThjcnZ5a2Y5aEhOZHYxSk9LZWhhUT09"],
    ["Capstone-1st", "08:55:00", [0,1,2,3,4], "https://southhills.zoom.us/j/92694121619?pwd=STkvOWNCc2JjbDZkR0JnejhGTzlzdz09"],
    ["Capstone-2nd", "09:55:00", [1,2,3], "https://southhills.zoom.us/j/92694121619?pwd=STkvOWNCc2JjbDZkR0JnejhGTzlzdz09"],
    ["Human Relations", "10:55:00", [0,1,3], "https://southhills.zoom.us/j/92000942141?pwd=R01xaVBZR2ZvRVJ1NHlKcldodnprdz09"],
    ["Oral Communications", "10:55:00", [2,4], "https://southhills.zoom.us/j/99435866675?pwd=Q0pjaXV6Y3hUSDZxNVZzTXB3aVYxZz09"],
    ["Intro to Business", "12:35:00", [0,1,2,3,4], "https://southhills.zoom.us/j/96188520164?pwd=c1hpQmI3UnB5eFZzM2tFeDJ2YWs4UT09"],
    ]
    
#Canvas vars
last_y = 0
row_height = 50
canvas_width =500
canvas_height = row_height + (50*len(classes))

#Create canvas
screen = tk.Canvas(root, width=canvas_width, height=canvas_height)
screen.pack()
root.title("Auto Zoomer")

#Time vars
Current_time = tk.StringVar()
Current_time.set(time.strftime("%H:%M:%S"))

#Draw top row
def draw_header():
    global last_y
    screen.create_rectangle(0, last_y, canvas_width, last_y + row_height, outline="black", fill="darkgrey")
    tk.Label(text="Class", bg="darkgrey").place(x=20, y=last_y+(row_height/3))
    tk.Label(text="Time", bg="darkgrey").place(x=200, y=last_y+(row_height/3))
    tk.Label(text="Weekdays", bg="darkgrey").place(x=300, y=last_y+(row_height/3))
    tk.Label(textvariable=Current_time,bg="darkgrey").place(x=400, y=last_y+(row_height/3))
    last_y += row_height

#Draw each class row
def draw_classes():
    global last_y
    for class_period in classes:
        screen.create_rectangle(0, last_y, canvas_width,last_y+row_height, outline="black", fill="grey")
        tk.Label(text=class_period[0], bg="grey").place(
            x=20, y=last_y+(row_height/3))
        tk.Label(text=class_period[1], bg="grey").place(
            x=200, y=last_y+(row_height/3))
        tk.Label(text=str(class_period[2]), bg="grey").place(
            x=300, y=last_y+(row_height/3))
        last_y += row_height

#Main logic loop
def update_loop():
    while (True): 
        #print("Current time is " + Current_time.get() )
        Current_time.set(time.strftime("%H:%M:%S"))
        for class_period in classes:
            if (Current_time.get() == class_period[1] and datetime.datetime.today().weekday() in class_period[2]):
                print("Launching meeting for %s" % (class_period[0]))
                webbrowser.open(class_period[3])
        root.update()
        time.sleep(1) 

draw_header()
draw_classes()
update_loop()


