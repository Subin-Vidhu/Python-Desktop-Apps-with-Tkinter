#!/usr/bin/python3

import tkinter
from tkinter import *

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Grid")

    l1 = Label(root, background="orange", width=15).grid(row=0,column=0,sticky='NSEW')
    l1 = Label(root, background="blue", width=15).grid(row=0,column=1,sticky='NSEW')
    l1 = Label(root, background="yellow", width=15).grid(row=0,column=2,sticky='NSEW')
    l1 = Label(root, background="red", width=15).grid(row=1,column=0,sticky='NSEW')
    l1 = Label(root, background="green", width=15).grid(row=1,column=1,sticky='NSEW')
    l1 = Label(root, background="purple", width=15).grid(row=1,column=2,sticky='NSEW')

    for x in range(0,3):
        for y in range(0,2):
            root.grid_columnconfigure(x,weight=1)
            root.grid_rowconfigure(y,weight=1)

    root.mainloop()
