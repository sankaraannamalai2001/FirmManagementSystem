from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
# import mysql.connector as mysql
from PIL import ImageTk
import smtplib
from tkinter import scrolledtext
import dbconnect
import statuspage


class Statusupdate:
    def __init__(self, root):
        self.root = root
        self.root.title("Login page")
        self.root.geometry("1600x850")
        self.root.resizable(True, True)
        self.bg = ImageTk.PhotoImage(file="updateStatus.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        frame_update = Frame(self.root, bg="white")
        frame_update.place(x=0, y=0, width=1600, height=800)
        canvas1 = Canvas(frame_update, width=1600,
                         height=850)

        canvas1.pack(fill="both", expand=True)
        canvas1.create_image(-50, -50, image=self.bg,
                             anchor="nw")

        self.company= Entry(frame_update, font=("poppins", 25), bg="#DBFFFA")
        self.company.place(x=750, y=145, width=475, height=45)

        self.city = Entry(frame_update, font=("poppins", 25), bg="#DBFFFA")
        self.city.place(x=750, y=208, width=475, height=45)

        self.text_area = scrolledtext.ScrolledText(frame_update,
                                                   wrap=tk.WORD,
                                                   width=80,
                                                   height=22,
                                                   font=("poppins",
                                                         15), bg="#DBFFFA")
        self.text_area.place(x=750, y=271)

        submit = Button(frame_update, command=self.back, text="BACK", bd=0, font=("poppins", 20, "bold"),
                        bg="#DBFFFA", fg="#40ACB2").place(x=590, y=650, width=291, height=61)
        submit = Button(frame_update, command=self.next, text="UPDATE STATUS", bd=0, font=("poppins", 20, "bold"),
                        bg="#DBFFFA", fg="#40ACB2").place(x=1000, y=650, width=291, height=61)
    def back(self):
        self.root.after(2000, statuspage.Status(self.root))
    def next(self):
        dbconnect.col.update_one({"username":self.uname},{$set:{"tasks":{"company":self.company.get(),"city":self.city}}})


