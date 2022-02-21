from tkinter import *
from PIL import ImageTk
import dbconnect
import auditornewtask
import details
import salaryauditor

class Articledetail:
    def __init__(self, root,uname):
        self.root = root
        self.uname= uname
        print(self.uname)
        self.root.title("Login page")
        self.root.geometry("1600x850")
        self.uname = uname
        self.root.resizable(True, True)
        self.bg = ImageTk.PhotoImage(file="articledetailspage.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        frame_article = Frame(self.root, bg="white")
        frame_article.place(x=0, y=0, width=1600, height=800)
        frame_inner = Frame(frame_article, bg="white")
        frame_inner.place(x=450, y=200, width=650, height=400)
        canvas1 = Canvas(frame_article, width=1600,
                         height=850)

        canvas1.pack(fill="both", expand=True)
        canvas1.create_image(-50, -50, image=self.bg,
                             anchor="nw")
        article = dbconnect.col.find_one({"username": self.uname})
        tasks = article["tasks"]
        name = Label(frame_article, text=article["username"], font=("poppins", 20), fg="#40ACB2",
                        bg="#ACEAE3").place(
            x=850, y=130)
        pno = Label(frame_article, text=article["phone"], font=("poppins", 20), fg="#40ACB2",
                        bg="#ACEAE3").place(
            x=850, y=185)

        company = Label(frame_article, text=tasks["company"], font=("poppins", 20), fg="#40ACB2",
                        bg="#ACEAE3").place(
            x=850, y=240)
        city = Label(frame_article, text=tasks["city"], font=("poppins", 20), fg="#40ACB2",
                     bg="#ACEAE3").place(
            x=850, y=305)
        description = Label(frame_article, text=tasks["description"], wraplength=500, font=("poppins", 20),
                            fg="#40ACB2",
                            bg="#ACEAE3").place(
            x=850, y=367)

        submit = Button(frame_article, command=self.update, text="UPDATE SALARY", bd=0, font=("poppins", 20, "bold"),
                        bg="#DBFFFA", fg="#40ACB2").place(x=570, y=580, width=291, height=61)
        submit = Button(frame_article, command=self.task, text="NEW TASK", bd=0, font=("poppins", 20, "bold"),
                        bg="#DBFFFA", fg="#40ACB2").place(x=1020, y=580, width=291, height=61)
        submit = Button(frame_article, command=self.back, text="BACK", bd=0, font=("poppins", 20, "bold"),
                        bg="#DBFFFA", fg="#40ACB2").place(x=800, y=660, width=291, height=61)


    def update(self):
        self.root.after(2000, salaryauditor.Salary(self.root, self.uname))
    def task(self):
        self.root.after(2000, auditornewtask.Task(self.root,self.uname))
    def back(self):
        self.root.after(2000, details.Detail(self.root))