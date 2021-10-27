from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
# import mysql.connector as mysql
from PIL import ImageTk
import smtplib
from tkinter import scrolledtext
import dbconnect
import articledetails


class Salary:
    def __init__(self, root,uname):
        self.root = root
        self.uname = uname
        self.root.title("Login page")
        self.root.geometry("1600x850")
        self.root.resizable(True, True)
        self.bg = ImageTk.PhotoImage(file="salarydetailsauditor.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        frame_salary = Frame(self.root, bg="white")
        frame_salary.place(x=0, y=0, width=1600, height=800)
        canvas1 = Canvas(frame_salary, width=1600,
                         height=850)

        canvas1.pack(fill="both", expand=True)
        canvas1.create_image(-50, -50, image=self.bg,
                             anchor="nw")
        article = dbconnect.col.find_one({"username": self.uname})
        sal = article["salary"]
        basic = StringVar(root, value=sal["basic"])
        ta = StringVar(root, value=sal["ta"])
        net=StringVar(root, value=int(sal["basic"])+int(sal["ta"]))
        self.basicpay = Entry(frame_salary, textvariable=basic, font=("poppins", 25), fg="#448078", bg="#DBFFFA")
        self.basicpay.place(x=850, y=155, width=200, height=40)

        self.ta = Entry(frame_salary, textvariable=ta,font=("poppins", 25), fg="#448078", bg="#DBFFFA")
        self.ta.place(x=850, y=207, width=200, height=40)

        self.netsalary = Entry(frame_salary,textvariable=net,font=("poppins", 25), fg="#448078", bg="#DBFFFA")
        self.netsalary.place(x=850, y=307, width=200, height=40)
        self.reqta=sal["reqta"]
        reqta = Label(frame_salary, text=sal["reqta"], font=("poppins", 20, "bold"), fg="#40ACB2",
                          bg="#ACEAE3").place(
            x=850, y=430)

        submit = Button(frame_salary, command=self.back, text="BACK", bd=0, font=("poppins", 20, "bold"),
                        bg="#DBFFFA", fg="#40ACB2").place(x=590, y=650, width=291, height=61)
        submit = Button(frame_salary, command=self.next, text="UPDATE", bd=0, font=("poppins", 20, "bold"),
                        bg="#DBFFFA", fg="#40ACB2").place(x=1000, y=650, width=291, height=61)

    def back(self):
        self.root.after(2000, articledetails.Articledetail(self.root, self.uname))
    def next(self):
        basic = self.basicpay.get();
        ta= self.ta.get();
        reqta = self.reqta;
        dbconnect.col.update_one({"username": self.uname},
                                 {"$set": {"salary": {"basic": basic, "ta": ta, "reqta": reqta}}})
        messagebox.showinfo("Success", "Salary updated successfully", parent=self.root)
        self.root.after(2000, articledetails.Articledetail(self.root, self.uname))

