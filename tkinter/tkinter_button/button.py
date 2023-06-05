#!/usr/bin/python3

# A button can be created with the function call tkinter.Button(). 

# You can then set the window, text, callback function, width, height and the state.

# tkinter.Button(root, text = "Quit", command=quit, width=50, height=5)

# It can be placed with the method .place(x,y)
import tkinter

def hello():
    print("Hello World")

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Hello World")
    root.geometry("500x400")
    
    mybutton = tkinter.Button(root, text = "Click me", command=hello, width=50, height=5, state=tkinter.ACTIVE)
    mybutton.place(x = 50,y = 50)

    gobutton = tkinter.Button(root, text = "Quit", command=quit, width=50, height=5)
    gobutton.place(x = 50,y = 150)
        
    root.mainloop()
