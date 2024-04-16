from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

greenLed = LED(14)
redLed = LED(15)
dualLed = LED(18)

win = Tk()
win.geometry("400x200")
win.title("LED TOGGLER")

myFont = tkinter.font.Font(family = 'helvetica', size = 12, weight = "bold")

var = IntVar()
var.set(1)
greenLed.on()

def ledToggle1():
    greenLed.on()
    redLed.off()
    dualLed.off()
    
def ledToggle2():
    greenLed.off()
    redLed.on()
    dualLed.off()
    
def ledToggle3():
    greenLed.off()
    redLed.off()
    dualLed.on()

Radiobutton(win, text="Green Led", variable=var, value=1, command=ledToggle1).pack()
Radiobutton(win, text="Red Led", variable=var, value=2,  command=ledToggle2).pack()
Radiobutton(win, text="Dual Led", variable=var, value=3,  command= ledToggle3).pack()

def Close():
    win.destroy()
    
exit_button = Button(win,text="Exit", command=Close).pack(pady=40)

mainloop()