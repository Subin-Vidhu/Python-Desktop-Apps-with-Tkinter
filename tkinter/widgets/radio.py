#!/usr/bin/python3

import tkinter
from tkinter import *

def callback():
   selection = str(var.get())
   label.config(text=selection) #update the label with the selection
   print(selection)
    
if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Tkinter")
    root.geometry("500x400")
    
    var = IntVar()
    button1 = Radiobutton(root, text="Option 1", variable=var, value=1, command=callback)
    #You can set the position in the pack function, anchor = (W,E,S,N). If you leave it out it'll be in the middle.
    button1.pack( anchor=W ) #pack the button to the left
    button2 = Radiobutton(root, text="Option 2", variable=var, value=2, command=callback)
    button2.pack( anchor=W )

    label = Label(root) #create a label to display the selection
    label.pack()

    root.mainloop()
