import tkinter
from tkinter import *

def func():
    value = int(wb.get())
    if value < 0 or value > 100:
        print("Value not in range")
        bt.config(state=DISABLED)  # Disable the button
    else:
        print(value)
        bt.config(state=NORMAL)  # Enable the button

def validate_spinbox(value):
    if value == "":
        bt.config(state=DISABLED)  # Disable the button if the entry is empty
    else:
        try:
            int_value = int(value)
            if int_value < 0 or int_value > 100:
                bt.config(state=DISABLED)  # Disable the button
            else:
                bt.config(state=NORMAL)  # Enable the button
        except ValueError:
            bt.config(state=DISABLED)  # Disable the button if the entry is not a valid integer
    return True

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Title World")
    root.geometry("300x300")

    vcmd = root.register(validate_spinbox)  # Register the validation function

    bt = Button(root, text="click", command=func, state=DISABLED)  # Start with button disabled
    bt.place(x=30, y=120)

    wb = Spinbox(root, from_=0, to=100, validate="key", validatecommand=(vcmd, "%P"))
    wb.place(x=30, y=100)



    root.mainloop()
