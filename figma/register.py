from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
# import mysql.connector as mysql
from PIL import ImageTk
import smtplib
from tkinter import scrolledtext
import dbconnect
import login



class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Login page")
        self.root.geometry("1600x850")
        self.root.resizable(True, True)
        self.bg = ImageTk.PhotoImage(file="background1.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        frame_register = Frame(self.root, bg="white")
        frame_register.place(x=0, y=0, width=1600, height=800)
        canvas1 = Canvas(frame_register, width=1600,
                         height=850)

        canvas1.pack(fill="both", expand=True)
        canvas1.create_image(-50, -50, image=self.bg,
                             anchor="nw")

        self.username1 = Entry(frame_register,  font=("poppins", 25), bg="#DBFFFA")
        self.username1.place(x=650, y=200, width=475, height=52)

        self.password1 = Entry(frame_register,  font=("poppins", 25), bg="#DBFFFA", show="*")
        self.password1.place(x=650, y=310, width=475, height=52)

        self.password2 = Entry(frame_register, font=("poppins", 25), bg="#DBFFFA", show="*")
        self.password2.place(x=650, y=430, width=475, height=52)

        self.phone = Entry(frame_register, font=("poppins", 25), bg="#DBFFFA")
        self.phone.place(x=650, y=530, width=475, height=52)

        submit = Button(frame_register, command=self.check_function, text="SIGNUP", bd=0, font=("poppins", 20, "bold"),
                        bg="#DBFFFA", fg="#40ACB2").place(x=760, y=650, width=291, height=61)


    def check_function(self):
        if self.username1.get() == "" or self.password1.get() == "" or self.password2.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            db = dbconnect.get_database()
            col = db["login"]
            profile = {
                "username": self.username1.get(),
                "password": self.password1.get(),
                "phone":self.phone.get()
            }
            col.insert_one(profile)
            self.root.after(2000, login.Login(self.root))
            self.root.destroy();


