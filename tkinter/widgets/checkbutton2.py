#!/usr/bin/python3

import tkinter
from tkinter import *

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Tkinter")
    root.geometry("500x400")

    var1 = tkinter.IntVar(value=1) #default value is 1, so the first check box is checked.
    var2 = tkinter.IntVar()
    var3 = tkinter.IntVar()
    var4 = tkinter.IntVar(value=1)

    Checkbutton(root, text="Python", variable=var1, width=50, height=3).grid(row=0, sticky=W)
    Checkbutton(root, text="Ruby", variable=var2, width=50, height=3).grid(row=1, sticky=W)
    Checkbutton(root, text="C++", variable=var3, width=50, height=3).grid(row=2, sticky=W)
    Checkbutton(root, text="C#", variable=var4, width=50, height=3).grid(row=3, sticky=W)
    
    root.mainloop()
