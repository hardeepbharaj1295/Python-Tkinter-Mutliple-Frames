from tkinter import *
import frame1
import frame2


class Dashboard:

    def __init__(self):
        self.win = Tk()
        self.win.geometry("600x400")
        self.win.title("Dashboard")

    def add_menu(self):
        self.mainmenu = Menu(self.win)
        self.win.config(menu=self.mainmenu)

        self.filemenu = Menu(self.mainmenu)
        self.mainmenu.add_cascade(label="File",menu=self.filemenu)

        self.filemenu.add_command(label="Frame 1",command=self.frame1)
        self.filemenu.add_command(label="Frame 2",command=self.frame2)

    def add_frame(self):
        self.frame = Frame(self.win)
        self.frame.place(x=50,y=50)

        self.label = Label(self.frame,text="Dashboard")
        self.label.grid(row=0, column=0)

        self.win.mainloop()

    def frame1(self):
        self.frame.destroy()
        f1 = frame1.Frame1(self.win)
        f1.addFrame()

    def frame2(self):
        self.frame.destroy()
        f2 = frame2.Frame2(self.win)
        f2.addFrame()


if __name__ == "__main__":
    x = Dashboard()
    x.add_menu()
    x.add_frame()