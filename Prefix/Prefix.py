from tkinter import *
from pathlib import Path


# Frame for the prefix to infix page
class Prefix(Frame):
    # constants
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    # class init method
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # image for error
        self.img_error = PhotoImage(file=self.relative_to_assets("error.png"))

        # creating the whole canvas of the frame
        canvas = Canvas(self, bg="#001524", height=551, width=395, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        # creating the bg image
        self.image_bg = PhotoImage(file=self.relative_to_assets("image_bg.png"))
        canvas.create_image(197.0, 275.0, image=self.image_bg)

        # creating the entry for expression
        self.expression = StringVar()
        self.expression.trace("w", self.reset_bg1_border)
        self.entry_imgExpression = PhotoImage(file=self.relative_to_assets("entry_expression.png"))
        self.entry_img = Label(self, image=self.entry_imgExpression, bg="#001524")
        self.entry_img.place(x=106.0, y=196.0)
        self.entry_Expression = Entry(self, textvariable=self.expression, bd=0, bg="#FFFFFF", fg="#000716",
                                      highlightthickness=0)
        self.entry_Expression.place(x=117.0, y=200.0, width=155, height=48)

        # creating the error message
        self.errorMsg = Label(canvas, anchor="nw", bg="#001524", fg="#CA1E1E", font=("Inter ExtraBold", 8 * -1))
        self.errorMsg.place(x=165.0, y=248.0)

        # creating the result text
        self.result = Label(canvas, anchor="nw", bg="#FFFFFF", fg="#000716", font=("Inter ExtraBold", 12 * -1))
        self.result.place(x=115.0, y=340.0)

        # creating the convert button
        self.button_imgConvert = PhotoImage(file=self.relative_to_assets("button_Convert.png"))
        button_Convert = Button(self, image=self.button_imgConvert, borderwidth=0, highlightthickness=0,
                                command=lambda: self.get_expression(controller), relief="flat")
        button_Convert.place(x=146.0, y=266.0, width=102.0, height=36.0)

        # creating the menu button
        self.button_imgMenu = PhotoImage(file=self.relative_to_assets("button_Menu.png"))
        button_Menu = Button(self, image=self.button_imgMenu, borderwidth=0, highlightthickness=0,
                             command=lambda: controller.show_frame("StartPage"), relief="flat")
        button_Menu.place(x=14.0, y=17.0, width=47.0, height=19.0)

    # for the path to be right
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    # storing the expression into a variable
    def get_expression(self, controller):
        self.result["text"] = ''
        expression = self.entry_Expression.get()
        if expression != "" and expression.count("/") or expression.count("+") \
                or expression.count("-") or expression.count("*"):
            try:
                result = self.prefix_to_infix(expression)
                self.result["text"] = result
                return
            except:
                self.errorMsg["text"] = "INVALID INPUT!"
                self.entry_img["image"] = self.img_error
                return
        self.errorMsg["text"] = "INVALID INPUT!"
        self.entry_img["image"] = self.img_error

    def prefix_to_infix(self, expression):
        # reverse the expression to convert it to postfix

        # initialize an empty stack
        stack = []

        # scanning the token from right to left
        for idx in reversed(range(len(expression))):
            char = expression[idx]
            # push the token in the stack if it is an operand
            if char not in ['+', '-', '*', '/'] and char != " ":
                stack.append(char)

            # pop the last two operands in the stack if the token is an operator
            elif char in ['+', '-', '*', '/'] and char != " ":
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                result = f"({operand_2}{char}{operand_1})"
                stack.append(result)

        # popping the last string in the stack
        result = stack.pop()
        # removing the unnecessary parenthesis
        result = result[1:-1]
        return result

    # function for clearing entries
    def clear_entries(self):
        self.entry_Expression.delete(0, END)

    # function for clearing the error message
    def reset_bg1_border(self, *args):
        self.entry_img.configure(image=self.entry_imgExpression)
        self.errorMsg.configure(text="")
