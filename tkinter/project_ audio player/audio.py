from tkinter import *
import time
from playsound import playsound

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.geometry("400x50")
        self.master.title("Audio Player")

        self.label = Label(self.frame, text="Song.wav", width=40)
        self.label.pack(side=LEFT)
        self.bt = Button(self.frame, text="Start", width=10, height=50, command=self.play)
        self.bt.pack(side=LEFT)

        self.frame.pack()

    def play(self):
        print('playing audio')    
        playsound('Song.wav')

def main(): 
    root = Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()


