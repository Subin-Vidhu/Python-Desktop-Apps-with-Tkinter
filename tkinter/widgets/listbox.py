#!/usr/bin/python3

import tkinter
from tkinter import *

def show():
    print(Input1.get())
    print(Input2.get())

if __name__ == "__main__":

    root = Tk()
    root.geometry("200x200")

    Label1 = Label(root, text="Name")
    Label1.grid(row=0, column=0, pady = 2)
    Input1 = Entry(root)
    Input1.grid(row=0, column=1, pady = 2)

    Label2 = Label(root, text="City")
    Label2.grid(row=1, column=0, pady = 2)
    Input2 = Entry(root)
    Input2.grid(row=1, column=1, pady = 2)

    Button(root, text='Show', command=show).grid(row=2, column=1, pady = 4)

    root.mainloop()