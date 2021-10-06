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
    def __init__(self,root):
        self.root=root
        self.root.title("Login page")
        self.root.geometry("1600x850")
        self.root.resizable(True, True)
        self.bg = ImageTk.PhotoImage(file="articledetails.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        frame_details = Frame(self.root, bg="white")
        frame_details.place(x=0, y=0, width=1600, height=800)

        canvas1 = Canvas(frame_details, width=1600,
                         height=850)
        frame_inner = Frame(frame_details, bg="#aceae3")
        frame_inner.place(x=450, y=200, width=400, height=250)

        canvas1.pack(fill="both", expand=True)
        canvas1.create_image(-50, -50, image=self.bg,
                             anchor="nw")

        self.tree = ttk.Treeview(frame_inner, column=("c1","c2"), show='headings')
        self.tree.column("#1", anchor=tk.CENTER)
        self.tree.heading("#1", text="Name")
        self.tree.column("#2", anchor=tk.CENTER)
        self.tree.heading("#2", text="Phone number")
        # self.tree.column("#3", anchor=tk.CENTER)
        # self.tree.heading("#3", text="Appointment Time")

        self.tree.pack()
        articles=dbconnect.col.find()
        for art in articles:
            print(art["username"])
            self.tree.insert("", tk.END, values=[art["username"],art["phone"]])
        # for row in records:
        #
root = Tk()
obj = Detail(root)
root.mainloop()