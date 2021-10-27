from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
# import mysql.connector as mysql
from PIL import ImageTk
import smtplib
from tkinter import scrolledtext
import login
import dbconnect
import statuspage

class Task:
    def __init__(self, root,uname):
        self.root = root
        self.uname=uname
        self.root.title("Login page")
        self.root.geometry("1600x850")
        self.root.resizable(True, True)
        self.bg = ImageTk.PhotoImage(file="newtask.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        frame_task = Frame(self.root, bg="white")
        frame_task.place(x=0, y=0, width=1600, height=800)
        canvas1 = Canvas(frame_task, width=1600,
                         height=850)

        canvas1.pack(fill="both", expand=True)
        canvas1.create_image(-50, -50, image=self.bg,
                             anchor="nw")
        article = dbconnect.col.find_one({"username": self.uname})
        tasks = article["newtask"]
        company = Label(frame_task, text=tasks["company"], font=("poppins", 20, "bold"), fg="#40ACB2",
                        bg="#ACEAE3").place(
            x=750, y=145)
        city = Label(frame_task, text=tasks["city"], font=("poppins", 20, "bold"), fg="#40ACB2",
                     bg="#ACEAE3").place(
            x=750, y=208)
        description = Label(frame_task, text=tasks["description"], wraplength=500, font=("poppins", 20, "bold"),
                            fg="#40ACB2",
                            bg="#ACEAE3").place(
            x=750, y=271)
        submit = Button(frame_task, command=self.back, text="BACK", bd=0, font=("poppins", 20, "bold"),
                        bg="#DBFFFA", fg="#40ACB2").place(x=800, y=600, width=270, height=55)


    def back(self):

        self.root.after(2000, statuspage.Status(self.root,self.uname))





