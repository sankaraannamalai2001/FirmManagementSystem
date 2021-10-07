from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
# import mysql.connector as mysql
from PIL import ImageTk
import smtplib
from tkinter import scrolledtext
import dbconnect
import login
import articledetails

class Detail:
    def __init__(self, root):
        self.root = root
        self.root.title("Login page")
        self.root.geometry("1600x850")
        self.root.resizable(True, True)
        self.bg = ImageTk.PhotoImage(file="articledetails2.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        frame_details = Frame(self.root, bg="white")
        frame_details.place(x=0, y=0, width=1600, height=800)

        canvas1 = Canvas(frame_details, width=1600,
                         height=850)

        canvas1.pack(fill="both", expand=True)
        canvas1.create_image(-50, -50, image=self.bg,
                             anchor="nw")
        frame_inner = Frame(frame_details, bg="#aceae3")
        frame_inner.place(x=450, y=200, width=400, height=250)
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                        font=('poppins', 13))  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('poppins', 15, 'bold'))  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        self.tree = ttk.Treeview(frame_inner, column=("c1", "c2"), show='headings', style="mystyle.Treeview")
        self.tree.column("#1", anchor=tk.CENTER)
        self.tree.heading("#1", text="Name")
        self.tree.column("#2", anchor=tk.CENTER)
        self.tree.heading("#2", text="Phone number")
        self.tree.bind('<ButtonRelease-1>', self.selectItem)
        self.tree.pack()
        articles = dbconnect.col.find()
        for art in articles:
            #print(art["username"])
            self.tree.insert("", tk.END, values=[art["username"], art["phone"]])

        submit = Button(frame_details, command=self.back, text="BACK", bd=0, font=("poppins", 20, "bold"),
                        bg="#DBFFFA", fg="#40ACB2").place(x=570, y=650, width=291, height=61)
        submit = Button(frame_details, command=self.view, text="VIEW", bd=0, font=("poppins", 20, "bold"),
                        bg="#DBFFFA", fg="#40ACB2").place(x=1020, y=650, width=291, height=61)

    def selectItem(self,a):
        curItem = self.tree.focus()
        self.cur=self.tree.item(curItem)


    def view(self):
        uname=self.cur["values"][0]
        #self.pid = (value[0][3])

        self.root.after(2000, articledetails.Articledetail(self.root,uname))
    def back(self):
        self.root.after(2000, login.Login(self.root))