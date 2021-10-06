from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
# import mysql.connector as mysql
from PIL import ImageTk
import smtplib
from tkinter import scrolledtext
import login
import dbconnect
import statusupdate
import salary

import newtask

class Task:
    def __init__(self, root):
        self.root = root
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

        self.username = Entry(frame_task, text="Username3", font=("poppins", 25), fg="#448078", bg="#DBFFFA")
        self.username.place(x=850, y=200, width=450, height=45)

        self.password = Entry(frame_task, text="Password3", font=("poppins", 25), fg="#448078", bg="#DBFFFA", show="*")
        self.password.place(x=850, y=380, width=450, height=45)