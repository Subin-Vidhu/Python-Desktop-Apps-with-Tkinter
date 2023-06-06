#!/usr/bin/python3

import tkinter
from tkinter import *

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Grid")

    w = 5
    h = 5

    for x in range(0,w):
        for y in range(0,h):
            label = Label(root, text="(" + str(x) + "," + str(y) + ")", width=15).grid(row=y,column=x,sticky='NSEW')

    for x in range(0,w):
        for y in range(0,h):
            root.grid_columnconfigure(x,weight=1)
            root.grid_rowconfigure(y,weight=1)

    root.mainloop()
