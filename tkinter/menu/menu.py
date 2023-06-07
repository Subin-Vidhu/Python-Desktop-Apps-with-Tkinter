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

editMenu = Menu(menubar, tearoff = 0)
editMenu.add_command(label="Copy", command=someFunc)
editMenu.add_command(label="Paste", command=someFunc)
menubar.add_cascade(label = "Edit", menu = editMenu)

aboutMenu = Menu(menubar, tearoff = 0)
aboutMenu.add_command(label="Help", command=someFunc)

submenu = Menu(tearoff = 0)
submenu.add_command(label="About", command=someFunc)
submenu.add_command(label="Online", command=someFunc)
aboutMenu.add_cascade(label='Import', menu=submenu)
               
menubar.add_cascade(label = "About", menu = aboutMenu)

root.config(menu = menubar)
root.mainloop()    