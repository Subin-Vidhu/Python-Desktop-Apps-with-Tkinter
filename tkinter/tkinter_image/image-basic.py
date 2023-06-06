from tkinter import *

root = Tk()
root.geometry("640x480")
root.title("Tkinter Window Title")

# You can load images with PhotoImage() method
# This can only load .gif, .pgm and .ppm

#  GIF, PGM, and PPM
imgicon = PhotoImage(file = r'images.gif')
img = Label(root, image=imgicon)
img.place(x=0,y=0) 

root.mainloop()    