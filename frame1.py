from tkinter import *


class Frame1:

    def __init__(self,wind):
        self.win = wind
        self.win.title("Login")

    def addFrame(self):
        self.frame = Frame(self.win)
        self.frame.place(x=50, y=50)

        self.label = Label(self.frame, text="Login")
        self.label.grid(row=0, column=0)

        self.win.mainloop()