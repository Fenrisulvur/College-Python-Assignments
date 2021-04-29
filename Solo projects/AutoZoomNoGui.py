import webbrowser
import time 
import datetime

#Classname, Class time, Days of week to launch, Zoom link to open
classes = [
    ["Python", "07:50:00", [0,1,2,3,4], "https://southhills.zoom.us/j/92936144602?pwd=QThjcnZ5a2Y5aEhOZHYxSk9LZWhhUT09"],
    ["Capstone-1st", "08:55:00", [0,1,2,3,4], "https://southhills.zoom.us/j/92694121619?pwd=STkvOWNCc2JjbDZkR0JnejhGTzlzdz09"],
    ["Capstone-2nd", "09:55:00", [2,3,4], "https://southhills.zoom.us/j/92694121619?pwd=STkvOWNCc2JjbDZkR0JnejhGTzlzdz09"],
    ["Human Relations", "10:55:00", [0,1,3], "https://southhills.zoom.us/j/92000942141?pwd=R01xaVBZR2ZvRVJ1NHlKcldodnprdz09"],
    ["Oral Communications", "10:55:00", [2,4], "https://southhills.zoom.us/j/99435866675?pwd=Q0pjaXV6Y3hUSDZxNVZzTXB3aVYxZz09"],
    ["Intro to Business", "12:35:00", [0,1,2,3,4], "https://southhills.zoom.us/j/96188520164?pwd=c1hpQmI3UnB5eFZzM2tFeDJ2YWs4UT09"],
    ]

Current_time = time.strftime("%H:%M:%S")
  
while (True): 
    print("Current time is " + Current_time )
    Current_time = time.strftime("%H:%M:%S")
    for class_period in classes:
        if (Current_time == class_period[1] and datetime.datetime.today().weekday() in class_period[2]):
            print("Launching meeting for %s" % (class_period[0]))
            webbrowser.open(class_period[3])
    time.sleep(1) 
