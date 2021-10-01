from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector as mysql
from PIL import ImageTk
import smtplib
from tkinter import scrolledtext


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login page")
        self.root.geometry("1600x800")
        self.root.resizable(True, True)
        frame_login = Frame(self.root, bg="white")
        frame_login.place(x=400, y=100, width=800, height=600)

        title = Label(frame_login, text="LOGIN", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(
            x=250, y=30)
        subtitle = Label(frame_login, text="Login here", font=("Goudy old style", 15, "bold"), fg="#1d1d1d",
                         bg="white").place(x=250, y=100)

        lbl_user = Label(frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="gray",
                         bg="white").place(x=250, y=140)
        self.username = Entry(frame_login, text="Username", font=("Goudy old style", 15), bg="#E7E6E6")
        self.username.place(x=250, y=170, width=320, height=35)

        lbl_user = Label(frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="gray",
                         bg="white").place(x=250, y=210)
        self.password = Entry(frame_login, text="Password", font=("Goudy old style", 15), bg="#E7E6E6", show="*")
        self.password.place(x=250, y=240, width=320, height=35)

        forget = Button(frame_login, command=self.login1, text="SIGN UP", bd=0, font=("Goudy old style", 15),
                        fg="#6162FF",
                        bg="white").place(x=250, y=280)
        submit = Button(frame_login, command=self.check_function, text="LOGIN", bd=0, font=("Goudy old style", 15),
                        bg="#6162FF", fg="white").place(x=250, y=320, width=180, height=40)

    def login1(self):
        root.after(2000, Login1(root))

    def check_function(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        user = self.username.get()
        pwd = self.password.get()
        con = mysql.connect(host="localhost", user="root", password="", database="hospital")
        cursor = con.cursor()
        cursor.execute("select username from user where username='" + user + "' and password='" + pwd + "'")
        record = cursor.fetchall()
        con.close()
        try:
            if self.username.get() == "doctor" and self.password.get() == "doctor":
                messagebox.showinfo("Welcome", f"Welcome {self.username.get()}")
                self.username.delete(0, 'end')
                self.password.delete(0, 'end')
                root.after(2000, Doctor1(root))
            elif record[0][0]:
                messagebox.showinfo("Welcome", f"Welcome {self.username.get()}")
                self.username.delete(0, 'end')
                self.password.delete(0, 'end')
                root.after(2000, SecondPage(root))
        except IndexError:
            messagebox.showerror("Error", "Invalid username or password", parent=self.root)


class Login1:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration page")
        self.root.geometry("1600x800")
        self.root.resizable(True, True)

        frame_login = Frame(self.root, bg="white")
        frame_login.place(x=400, y=100, width=800, height=600)

        title = Label(frame_login, text="REGISTER", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(
            x=250, y=30)

        lbl_user = Label(frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="gray",
                         bg="white").place(x=250, y=140)
        self.username = Entry(frame_login, text="Username", font=("Goudy old style", 15), bg="#E7E6E6")
        self.username.place(x=250, y=170, width=320, height=35)

        lbl_user = Label(frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="gray",
                         bg="white").place(x=250, y=210)
        self.password = Entry(frame_login, text="Password", font=("Goudy old style", 15), bg="#E7E6E6", show="*")
        self.password.place(x=250, y=240, width=320, height=35)

        lbl_user = Label(frame_login, text="Retype Password", font=("Goudy old style", 15, "bold"), fg="gray",
                         bg="white").place(x=250, y=285)
        self.rpassword = Entry(frame_login, text="rPassword", font=("Goudy old style", 15), bg="#E7E6E6", show="*")
        self.rpassword.place(x=250, y=320, width=320, height=35)

        submit = Button(frame_login, command=self.check_function, text="REGISTER", bd=0, font=("Goudy old style", 15),
                        bg="#6162FF", fg="white").place(x=250, y=390, width=180, height=40)

    def check_function(self):
        if self.username.get() == "" or self.password.get() == "" or self.rpassword.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.password.get() != self.rpassword.get():
            messagebox.showerror("Error", "Password doesn't match", parent=self.root)
            self.password.delete(0, 'end')
            self.rpassword.delete(0, 'end')
        else:
            pname = self.username.get();
            ppass = self.password.get();
            con = mysql.connect(host="localhost", user="root", password="", database="hospital")
            cursor = con.cursor()
            sql = "INSERT INTO user (username, password) VALUES (%s, %s)"
            val = (pname, ppass)
            cursor.execute(sql, val)
            cursor.execute("commit");
            self.username.delete(0, 'end')
            self.password.delete(0, 'end')
            self.rpassword.delete(0, 'end')
            messagebox.showinfo("Details Status", "Registered sucessfully")
            root.after(6000, Login(root))
            con.close();


root = Tk()
obj = Login(root)
root.mainloop()