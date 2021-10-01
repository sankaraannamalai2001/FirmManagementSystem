from tkinter import *
import tkinter as tk
class Login:
    def btn_clicked(self):
        print("Button Clicked")

    def __init__(self, root):
        self.root = root
        self.root.title("Login page")
        self.root.geometry("1600x800")
        self.root.resizable(True, True)
        frame_login = Frame(self.root, bg="white")
        frame_login.place(x=0, y=0, width=1550, height=750)
        canvas = Canvas(
            frame_login,
            bg = "#ffffff",
            height = 957,
            width = 1558,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = f"background.png")
        background = canvas.create_image(

            744.0, 412.5,
            image=background_img)

        img0 = PhotoImage(file = f"img0.png")
        b0 = Button(
            frame_login,
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
        bg = "#dbfffa",
            command = self.btn_clicked,
            relief = "flat")

        b0.place(
            x = 738, y = 508,
            width = 291,
            height = 59)

        img1 = PhotoImage(file = f"img1.png")
        b1 = Button(
            frame_login,
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
        bg = "#dbfffa",
            command = self.btn_clicked,
            relief = "flat")

        b1.place(
            x = 738, y = 661,
            width = 291,
            height = 61)

        entry0_img = PhotoImage(file = f"img_textBox0.png")
        entry0_bg = canvas.create_image(

            879.5, 312.5,
            image = entry0_img)

        entry0 = Entry(
            frame_login,
            bd = 0,
            bg = "#dbfffa",
            highlightthickness = 0)

        entry0.place(
            x = 642, y = 289,
            width = 475,
            height = 45)

        entry1_img = PhotoImage(file = f"img_textBox1.png")
        entry1_bg = canvas.create_image(

            879.5, 433.5,
            image = entry1_img)

        entry1 = Entry(
            frame_login,
            bd = 0,
            bg = "#dbfffa",
            highlightthickness = 0)

        entry1.place(
            x = 642, y = 411,
            width = 475,
            height = 43)
root = Tk()
obj = Login(root)
root.mainloop()