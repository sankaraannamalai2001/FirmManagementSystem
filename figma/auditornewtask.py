from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import ImageTk
from tkinter import scrolledtext
import dbconnect
import articledetails


class Task:
    def __init__(self, root,uname):
        self.root = root
        self.uname=uname
        self.root.title("Login page")
        self.root.geometry("1600x850")
        self.root.resizable(True, True)
        self.bg = ImageTk.PhotoImage(file="newtaskauditor.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        frame_task = Frame(self.root, bg="white")
        frame_task.place(x=0, y=0, width=1600, height=800)
        canvas1 = Canvas(frame_task, width=1600,
                         height=850)

        canvas1.pack(fill="both", expand=True)
        canvas1.create_image(-50, -50, image=self.bg,
                             anchor="nw")

        self.company = Entry(frame_task,  text="comapany", font=("poppins", 25), fg="#448078", bg="#DBFFFA")
        self.company.place(x=800, y=153, width=450, height=40)

        self.city= Entry(frame_task, text="Password3", font=("poppins", 25), fg="#448078", bg="#DBFFFA")
        self.city.place(x=800, y=207, width=450, height=40)

        self.text_area = scrolledtext.ScrolledText(frame_task,
                                                   wrap=tk.WORD,
                                                   width=72,
                                                   height=22,
                                                   font=("Times New Roman",
                                                         10), bg="#DBFFFA")
        self.text_area.place(x=800, y=265)

        submit = Button(frame_task, command=self.back, text="BACK", bd=0, font=("poppins", 20, "bold"),
                        bg="#DBFFFA", fg="#40ACB2").place(x=570, y=650, width=291, height=61)
        submit = Button(frame_task, command=self.allot, text="ALLOT", bd=0, font=("poppins", 20, "bold"),
                        bg="#DBFFFA", fg="#40ACB2").place(x=1020, y=650, width=291, height=61)


    def back(self):
        self.root.after(2000, articledetails.Articledetail(self.root,self.uname))
    def allot(self):
        com = self.company.get();
        cit = self.city.get();
        desc = self.text_area.get("1.0", tk.END);
        dbconnect.col.update_one({"username": self.uname},
                                 {"$set": {"newtask": {"company": com, "city": cit, "description": desc}}})
        messagebox.showinfo("Success", "New task added successfully", parent=self.root)
        self.root.after(2000, articledetails.Articledetail(self.root,self.uname))