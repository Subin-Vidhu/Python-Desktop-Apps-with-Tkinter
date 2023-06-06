#!/usr/bin/python3

import tkinter
from tkinter import *

def func():
    print(var.get())

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Title World")
    root.geometry("300x300")

    var = DoubleVar()
    scale = Scale( root, variable = var ) 
    scale.pack(anchor=CENTER)

    button = Button(root, text="How much", command=func)
    button.pack(anchor=CENTER)

    root.mainloop()
