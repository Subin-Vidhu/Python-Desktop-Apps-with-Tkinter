#!/usr/bin/python3

import tkinter
from tkinter import *

def hello():
    print("Hello World")

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Tkinter")
    root.geometry("500x400")

    var1 = tkinter.IntVar() #Check boxes can be added to a Tkinter window. They are linked to a integer value, tkinter.IntVal().
    var2 = tkinter.IntVar()
    Checkbutton(root, text="Male", variable=var1).grid(row=0, sticky=W)
    Checkbutton(root, text="Female", variable=var2).grid(row=1, sticky=W)
    
    root.mainloop()
