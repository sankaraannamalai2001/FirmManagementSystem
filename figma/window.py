from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1558x957")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 957,
    width = 1558,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    744.0, 412.5,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
bg = "#dbfffa",
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 738, y = 508,
    width = 291,
    height = 59)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
bg = "#dbfffa",
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 738, y = 661,
    width = 291,
    height = 61)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    879.5, 312.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#dbfffa",
    highlightthickness = 0)

entry0.place(
    x = 642, y = 289,
    width = 475,
    height = 45)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    879.5, 433.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#dbfffa",
    highlightthickness = 0)

entry1.place(
    x = 642, y = 411,
    width = 475,
    height = 43)

window.resizable(True, True)
window.mainloop()
