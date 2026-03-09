import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter as tk

# Import next page
from dataupload import ViewData


# ---------------- LOGIN FUNCTION ----------------
def act():
    x = admin_var.get()
    y = pass_var.get()

    if x == "Admin" and y == "Admin":
        messagebox.showinfo("Success", "Login Successful!")
        winadmin.destroy()
        ViewData()
    else:
        messagebox.showerror("Error", "Invalid Username or Password")


# ---------------- MAIN WINDOW ----------------
winadmin = Tk()
winadmin.title("Food Calorie Estimation - Admin Login")
winadmin.geometry("1100x1000")
winadmin.resizable(False, False)
winadmin.configure(bg="#ecf0f1")


# ---------------- SAFE BACKGROUND IMAGE LOADING ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
bg_path = os.path.join(BASE_DIR, "background.png")

# Debug print (optional – can remove later)
print("Loading background from:", bg_path)

bg_image = Image.open(bg_path)
bg_image = bg_image.resize((1100, 1000))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(winadmin, image=bg_photo)
bg_label.image = bg_photo
bg_label.place(x=0, y=0)


# ---------------- HEADER ----------------
Label(
    winadmin,
    text="FOOD CALORIE ESTIMATION",
    bg="#2c3e50",
    fg="white",
    font=("Segoe UI", 22, "bold"),
    padx=30,
    pady=15
).place(x=300, y=40)


# ---------------- LOGIN FRAME ----------------
login_frame = Frame(winadmin, bg="white", bd=2, relief=RIDGE)
login_frame.place(x=350, y=250, width=400, height=320)

Label(
    login_frame,
    text="Admin Login",
    bg="white",
    fg="#2c3e50",
    font=("Segoe UI", 16, "bold")
).place(x=120, y=20)


# ---------------- VARIABLES ----------------
admin_var = StringVar()
pass_var = StringVar()


# ---------------- USERNAME ----------------
Label(
    login_frame,
    text="Username",
    bg="white",
    fg="#34495e",
    font=("Segoe UI", 11, "bold")
).place(x=50, y=80)

Entry(
    login_frame,
    width=30,
    textvariable=admin_var,
    font=("Segoe UI", 11),
    bd=2
).place(x=50, y=110)


# ---------------- PASSWORD ----------------
Label(
    login_frame,
    text="Password",
    bg="white",
    fg="#34495e",
    font=("Segoe UI", 11, "bold")
).place(x=50, y=160)

Entry(
    login_frame,
    width=30,
    show="*",
    textvariable=pass_var,
    font=("Segoe UI", 11),
    bd=2
).place(x=50, y=190)


# ---------------- LOGIN BUTTON ----------------
Button(
    login_frame,
    text="LOGIN",
    font=("Segoe UI", 12, "bold"),
    bg="#1abc9c",
    fg="white",
    activebackground="#16a085",
    activeforeground="white",
    bd=0,
    width=18,
    height=2,
    cursor="hand2",
    command=act
).place(x=100, y=240)


# ---------------- MAIN LOOP ----------------
winadmin.mainloop()
