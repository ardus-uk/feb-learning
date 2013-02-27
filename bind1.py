#!/usr/bin/python

#Example 7-1. Capturing clicks in a window

# File: bind1.py
# from http://www.pythonware.com/library/tkinter/introduction/hello-tkinter.htm

from Tkinter import *

root = Tk()

def callback(event):
    print "clicked at (", event.x, ",", event.y ,")"

myLabel = Label(root, foreground="white", background="black", text="Click the yellow area, above this text")

frame = Frame(root, width=200, height=150, background="yellow")
frame.bind("<Button-1>", callback)
frame.pack()
myLabel.pack()

root.mainloop()