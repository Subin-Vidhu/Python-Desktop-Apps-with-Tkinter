from tkinter import *

root = Tk()
root.geometry("640x480")
root.title("Tkinter Window Title")

#  GIF, PGM, and PPM
imgicon = PhotoImage(file = r'image.gif')
img = Label(root, image=imgicon)
img.place(x=0,y=0) 

root.mainloop()    