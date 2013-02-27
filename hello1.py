#!/usr/bin/python

# File: hello1.py
# from http://www.pythonware.com/library/tkinter/introduction/hello-tkinter.htm

from Tkinter import *

root = Tk()

w = Label(root, text="Hello, world!")
w.pack()

root.mainloop()