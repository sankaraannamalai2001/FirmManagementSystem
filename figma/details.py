from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
# import mysql.connector as mysql
from PIL import ImageTk
import smtplib
from tkinter import scrolledtext
import dbconnect
import login



class Detail:
    def __init__(self, root):
        self.root = root
        self.root.title("Login page")
        self.root.geometry("1600x850")
        self.root.resizable(True, True)
        self.bg = ImageTk.PhotoImage(file="articledetails.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        frame_datails = Frame(self.root, bg="white")
        frame_datails.place(x=0, y=0, width=1600, height=800)
        canvas1 = Canvas(frame_datails, width=1600,
                         height=850)

        canvas1.pack(fill="both", expand=True)
        canvas1.create_image(-50, -50, image=self.bg,
                             anchor="nw")

