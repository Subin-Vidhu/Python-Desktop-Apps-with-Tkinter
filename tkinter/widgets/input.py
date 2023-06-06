#!/usr/bin/python3

import tkinter
from tkinter import *

def click():
    print(tinput1.get())
    print(tinput2.get())
    
if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Enter Text: ")
    root.geometry("500x400")

    # add label
    label = tkinter.Label(root, text="Enter text: ")
    label.grid(row=0,column=0)

    label = tkinter.Label(root, text="Enter City: ")
    label.grid(row=1,column=0)

    # add text input
    tinput1 = Entry(root)
    tinput1.grid(row=0,column=1)
    tinput2 = Entry(root)
    tinput2.grid(row=1,column=1)

    # add button
    b = Button(root, text="Click", command=click)
    b.grid(row=2,column=1)
    
    root.mainloop()
