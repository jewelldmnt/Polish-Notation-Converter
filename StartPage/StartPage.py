from tkinter import *
from pathlib import Path


# Frame for the home page
class StartPage(Frame):
    # constants
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    # home page class init method
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # creating the whole canvas of the frame
        canvas = Canvas(self, bg="#001524", height=551, width=395, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        # creating the bg image
        self.image_bg = PhotoImage(file=self.relative_to_assets("bg.png"))
        canvas.create_image(197.0, 275.0, image=self.image_bg)

        # creating the postfix to infix button
        self.imgPostToIn = PhotoImage(file=self.relative_to_assets("button_postToIn.png"))
        button_post = Button(self, image=self.imgPostToIn, borderwidth=0, highlightthickness=0,
                             command=lambda: controller.show_frame("Postfix"), relief="flat")
        button_post.place(x=101.0, y=256.0, width=192.0, height=61.0)

        # creating the prefix to infix button
        self.imgPreToIn = PhotoImage(file=self.relative_to_assets("button_preToIn.png"))
        button_PreToIn = Button(self, image=self.imgPreToIn, borderwidth=0, highlightthickness=0,
                                command=lambda: controller.show_frame("Prefix"), relief="flat")
        button_PreToIn.place(x=102.0, y=322.0, width=192.0, height=61.0)

    # for the path to be right
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
