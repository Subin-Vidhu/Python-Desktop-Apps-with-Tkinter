#!/usr/bin/python3

import tkinter
from tkinter import *

def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print('You selected item %d: "%s"' % (index, value))
    
if __name__ == "__main__":

    root = Tk()
    root.geometry("200x200")


    Lb1 = Listbox(root)

    Lb1.insert(1, "Python")
    Lb1.insert(2, "Perl")
    Lb1.insert(3, "C")
    Lb1.insert(4, "PHP")
    Lb1.insert(5, "JSP")

    # Lb1.bind('<<ListboxSelect>>', lambda event: print(Lb1.curselection()))
    Lb1.bind('<<ListboxSelect>>', onselect)
    Lb1.grid(row=0, column=2, pady = 2)
    Lb1.grid(row=1, column=2, pady = 2)
    Lb1.grid(row=2, column=2, pady = 2)
    Lb1.grid(row=3, column=2, pady = 2)
    Lb1.grid(row=4, column=2, pady = 2)


    root.mainloop()