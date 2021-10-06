from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
# import mysql.connector as mysql
from PIL import ImageTk
import smtplib
from tkinter import scrolledtext
import dbconnect
import statuspage


class Salary:
    def __init__(self, root,uname):
        self.root = root
        self.uname = uname
        self.root.title("Login page")
        self.root.geometry("1600x850")
        self.root.resizable(True, True)
        self.bg = ImageTk.PhotoImage(file="salary.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        frame_salary = Frame(self.root, bg="white")
        frame_salary.place(x=0, y=0, width=1600, height=800)
        canvas1 = Canvas(frame_salary, width=1600,
                         height=850)

        canvas1.pack(fill="both", expand=True)
        canvas1.create_image(-50, -50, image=self.bg,
                             anchor="nw")
        article = dbconnect.col.find_one({"username": self.uname})
        salary = article["salary"]
        self.basic=salary["basic"]
        self.ta=salary["ta"]
        netsalary=int(salary["basic"])+int(salary["ta"])
        basicpay = Label(frame_salary, text=salary["basic"], font=("poppins", 20, "bold"), fg="#40ACB2",
                        bg="#ACEAE3").place(
            x=910, y=145)
        TA = Label(frame_salary, text=salary["ta"], font=("poppins", 20, "bold"), fg="#40ACB2",
                     bg="#ACEAE3").place(
            x=910, y=208)
        netsalary = Label(frame_salary, text=str(netsalary), font=("poppins", 20, "bold"), fg="#40ACB2",
                   bg="#ACEAE3").place(
            x=910, y=311)

        self.req = Entry(frame_salary,font=("poppins", 25), bg="#DBFFFA")
        self.req.place(x=850, y=424, width=345, height=52)

        submit = Button(frame_salary, command=self.back, text="BACK", bd=0, font=("poppins", 20, "bold"),
                        bg="#DBFFFA", fg="#40ACB2").place(x=590, y=650, width=291, height=61)
        submit = Button(frame_salary, command=self.next, text="REQUEST", bd=0, font=("poppins", 20, "bold"),
                        bg="#DBFFFA", fg="#40ACB2").place(x=1000, y=650, width=291, height=61)


    def next(self):
        reqta=self.req.get();
        dbconnect.col.update_one({"username":self.uname},{"$set":{"salary":{"basic":self.basic,"ta":self.ta,"reqta":reqta}}})
        self.root.after(2000, statuspage.Status(self.root, self.uname))
    def back(self):
        self.root.after(2000, statuspage.Status(self.root,self.uname))


