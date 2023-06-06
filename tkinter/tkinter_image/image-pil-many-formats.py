from tkinter import *
from PIL import Image, ImageTk #Use PIL (Python Image Library) to load more image formats

root = Tk()
root.geometry("640x480")
root.title("Tkinter Window Title")

PIL_image = Image.open("1234.jpg")
render = ImageTk.PhotoImage(PIL_image)
img = Label(root, image=render)
img.place(x=0,y=0) 

root.mainloop()    