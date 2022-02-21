from tkinter import *
from PIL import ImageTk
import login
import dbconnect
import statusupdate
import salary
import newtask

class Status:
    def __init__(self, root,uname):
        self.root = root
        self.uname=uname
        self.root.title("Login page")
        self.root.geometry("1600x850")
        self.root.resizable(True, True)
        self.bg = ImageTk.PhotoImage(file="statuspage.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        frame_status = Frame(self.root, bg="white")
        frame_status.place(x=0, y=0, width=1600, height=800)
        canvas1 = Canvas(frame_status, width=1600,
                         height=850)

        canvas1.pack(fill="both", expand=True)
        canvas1.create_image(-50, -50, image=self.bg,
                             anchor="nw")
        article = dbconnect.col.find_one({"username": self.uname})
        tasks = article["tasks"]
        #print(tasks["company"])
        company = Label(frame_status, text=tasks["company"], font=("poppins", 20), fg="#40ACB2",
                      bg="#ACEAE3").place(
            x=750, y=145)
        city = Label(frame_status, text=tasks["city"], font=("poppins", 20), fg="#40ACB2",
                      bg="#ACEAE3").place(
            x=750, y=208)
        description = Label(frame_status, text=tasks["description"],wraplength=500, font=("poppins", 20), fg="#40ACB2",
                      bg="#ACEAE3").place(
            x=750, y=271)



        submit = Button(frame_status, command=self.salary, text="SALARY DETAILS", bd=0, font=("poppins", 20, "bold"),
                        bg="#DBFFFA", fg="#40ACB2").place(x=570, y=550, width=291, height=61)
        submit = Button(frame_status, command=self.update, text="UPDATE STATUS", bd=0, font=("poppins", 20, "bold"),
                        bg="#DBFFFA", fg="#40ACB2").place(x=1020, y=550, width=291, height=61)
        submit = Button(frame_status, command=self.back, text="LOGOUT", bd=0, font=("poppins", 20, "bold"),
                        bg="#DBFFFA", fg="#40ACB2").place(x=700, y=630, width=200, height=51)
        submit = Button(frame_status, command=self.new, text="NEW TASK", bd=0, font=("poppins", 20, "bold"),
                        bg="#DBFFFA", fg="#40ACB2").place(x=950, y=630, width=200, height=51)

    def new(self):
        self.root.after(2000, newtask.Task(self.root, self.uname))


    def salary(self):
        self.root.after(2000, salary.Salary(self.root, self.uname))

    def update(self):
        self.root.after(2000, statusupdate.Statusupdate(self.root,self.uname))

    def back(self):
        self.root.after(2000, login.Login(self.root))