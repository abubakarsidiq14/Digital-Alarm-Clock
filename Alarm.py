from tkinter import *
from PIL import ImageTk,Image
import time
import pygame as pg

pg.mixer.init()

root=Tk()
root.title("Digital Alarm Clock Of 24 Hour")
root.geometry("500x500")

alarmtime =StringVar()

def alarm():
    Alarm = alarmtime.get()
    AlarmT = Alarm
    CurrentTime = time.strftime("%H:%M")

    while AlarmT != CurrentTime:
        CurrentTime = time.strftime("%H:%M")

    if AlarmT == CurrentTime:
        pg.mixer.music.load('GUITAR.WAV')
        pg.mixer.music.play()

def stop():
	pg.mixer.music.stop()

frame = Frame(root, width=60, height=40)
frame.place(x=100,y=80)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("images.jpg"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()

Label(root,text="Digital Alarm Clock",font="Times 24 bold").place(x=100,y=30)

Label(root,text="Enter Time : ",font="Times 18 ").place(x=80,y=300)
Entry(root,textvariable=alarmtime,width=18).place(x=250,y=310)


Button(root,text="Set Alarm",font="Times 18 bold",command=alarm).place(x=250,y=360)
Button(root,text="Ok",font="Times 18 bold",command=stop).place(x=100,y=360)

Label(root,text="Click Ok To Stop Alarm",font="Times 14 ").place(x=80,y=420)

root.mainloop()