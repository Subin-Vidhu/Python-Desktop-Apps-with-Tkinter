from tkinter import *
from tkinter import messagebox

def fileNew():
    print("New file")

def someFunc():
    print('Something')

root = Tk()
menubar = Menu(root)
fileMenu = Menu(menubar, tearoff = 0)
fileMenu.add_command(label="New", command=fileNew)
fileMenu.add_command(label = "Open", command=someFunc)
fileMenu.add_command(label = "Save", command=someFunc)
fileMenu.add_command(label = "Close", command=someFunc)
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command = root.quit)
menubar.add_cascade(label = "File", menu = fileMenu)
root.config(menu = menubar)

root.mainloop()    