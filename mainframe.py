# importing the required libraries/modules
from tkinter import *
from Postfix.Postfix import Postfix
from StartPage.StartPage import StartPage
from Prefix.Prefix import Prefix


# class for the main frame
class mainframe(Tk):
    # init method of the class MainFrame
    def __init__(self, *args, **kwargs):
        # init method of the tk class
        Tk.__init__(self, *args, **kwargs)

        # creating a container for all
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # creating a dictionary for page objects
        self.frames = {}

        # looping in every page/class and creating an object of it
        # then storing the class name as the key
        # and the object of it as the value
        for f in {StartPage, Postfix, Prefix}:
            page_name = f.__name__
            frame = f(container, self)
            frame.grid(row=0, column=0, sticky="NSEW")
            self.frames[page_name] = frame

        self.show_frame("StartPage")

    # showing the current frame above everything
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


# initialize main window app
window = mainframe()
window.geometry("395x551")
window.resizable(0,0)

window.mainloop()