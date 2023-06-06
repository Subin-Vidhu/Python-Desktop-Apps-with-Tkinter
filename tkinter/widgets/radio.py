#!/usr/bin/python3

import tkinter
from tkinter import *

def callback():
   selection = str(var.get())
   print(selection)
    
if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Tkinter")
    root.geometry("500x400")
    
    var = IntVar()
    button1 = Radiobutton(root, text="Option 1", variable=var, value=1, command=callback)
    button1.pack( anchor=W )

    root.mainloop()
