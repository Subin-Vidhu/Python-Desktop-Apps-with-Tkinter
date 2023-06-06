#!/usr/bin/python3

import tkinter
from tkinter import *

def click():
    print(tinput.get())
    
if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Enter Text: ")
    root.geometry("500x400")

    # add label
    label = tkinter.Label(root, text="Enter text: ")
    label.grid(row=0,column=0)

    # add text input
    tinput = Entry(root)
    tinput.grid(row=0,column=1)

    # add button
    b = Button(root, text="Click", command=click)
    b.grid(row=1,column=1)
    
    root.mainloop()
