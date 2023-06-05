from tkinter import *
from tkinter import messagebox

root = Tk()
root.withdraw()

#1
result = messagebox.askquestion("Question","Are You sure?")
print("result of ask question",result)
if result == "yes":
    print("You clicked yes.")
else:
    print("You clicked no.")

#2
result = messagebox.askokcancel("OkCancel","Continue?")
print("result of ask ok cancel",result)
if result is True:
    print("Continue")
else:
    print("Cancel")

#3
result = messagebox.askretrycancel("Warning","Failed, try again?")
print("result of ask retry cancel",result)
if result is True:
    print("Trying")
else:
    print("Give up")
    
#4
result = messagebox.askyesno("YesNo","Continue?")
print("result of ask yes no",result)
if result is True:
    print("Continue")
else:
    print("Cancel")

#5
result = messagebox.askyesnocancel("YesNoCancel","Continue?")
print("result of ask yes no cancel",result)
if result is True:
    print("Continue")
elif result is False:
    print("Cancel")
else:
    print("Cancel")
