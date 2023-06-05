from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("640x480")
root.title("Tkinter Window Title")

PIL_image = Image.open("image.gif")
render = ImageTk.PhotoImage(PIL_image)
img = Label(root, image=render)
img.place(x=0,y=0) 

root.mainloop()    