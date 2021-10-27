from tkinter import *
from captcha.image import ImageCaptcha
import tkinter as tk
from tkinter import messagebox, ttk
# import mysql.connector as mysql
from PIL import ImageTk
import smtplib
from tkinter import scrolledtext
import dbconnect
import login
import string
import random


class Captcha:
    def __init__(self, root):
        self.root = root
        self.root.title("Login page")
        self.root.geometry("1600x850")
        self.root.resizable(True, True)
        self.bg = ImageTk.PhotoImage(file="captcha.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        frame_captcha = Frame(self.root, bg="white")
        frame_captcha.place(x=0, y=0, width=1600, height=800)
        canvas1 = Canvas(frame_captcha, width=1600,
                         height=850)
        #canvas
        canvas1.pack(fill="both", expand=True)
        canvas1.create_image(-50, -50, image=self.bg,
                             anchor="nw")
        self.cap = Entry(frame_captcha, font=("poppins", 25), bg="#A1DCD4")
        self.cap.place(x=747, y=380, width=407, height=61)

        S = 5

        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
        random_word = str(ran)


        image = ImageCaptcha(width=280, height=90)
        captcha_text = ran
        data = image.generate(captcha_text)
        image.write(captcha_text, 'CAPTCHA1.png')

        submit = Button(frame_captcha, command=self.check_function, text="SIGNUP", bd=0, font=("poppins", 20, "bold"),
                        bg="#A1DCD4", fg="#40ACB2").place(x=790, y=530, width=291, height=61)

    def check_function(self):
        pass
    def print_selection(self):
        pass

root = Tk()
obj = Captcha(root)
root.mainloop()