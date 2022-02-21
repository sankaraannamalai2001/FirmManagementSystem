from tkinter import *
from tkinter import messagebox, ttk
from PIL import ImageTk
import details
import login
class Otp:
    def __init__(self, root, otp1):
        self.root = root
        self.otp1 = otp1
        self.root.title("Login page")
        self.root.geometry("1600x850")
        self.root.resizable(True, True)
        self.bg = ImageTk.PhotoImage(file="otp.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        frame_otp = Frame(self.root, bg="white")
        frame_otp.place(x=0, y=0, width=1600, height=800)
        canvas1 = Canvas(frame_otp, width=1600,
                         height=850)

        canvas1.pack(fill="both", expand=True)
        canvas1.create_image(-50, -50, image=self.bg,
                             anchor="nw")

        self.company = Entry(frame_otp, font=("poppins", 25), bg="#DBFFFA", fg="#448078", )
        self.company.place(x=830, y=345, width=205, height=45)


        submit = Button(frame_otp, command=self.back, text="BACK", bd=0, font=("poppins", 20, "bold"),
                        bg="#DBFFFA", fg="#40ACB2").place(x=590, y=650, width=291, height=61)
        submit = Button(frame_otp, command=self.next, text="VERIFY", bd=0, font=("poppins", 20, "bold"),
                        bg="#DBFFFA", fg="#40ACB2").place(x=1000, y=650, width=291, height=61)

    def back(self):
        self.root.after(2000, login.Login(self.root))
    def next(self):
        otp=self.company.get()
        if otp==self.otp1:
            self.root.after(2000, details.Detail(self.root))
        else:
            messagebox.showerror("Error", "OTP entered is incorrect", parent=self.root)


