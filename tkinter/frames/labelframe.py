#!/usr/bin/python3

import tkinter
from tkinter import *

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Title World")
    root.geometry("300x300")

    labelframe = LabelFrame(root, text="Tkinter Coding")
    labelframe.pack(fill="both", expand="yes")
 
    bt = Button(labelframe, text="click")
    bt.pack()

    bt2 = Button(labelframe, text="click")
    bt2.pack()


    root.mainloop()
