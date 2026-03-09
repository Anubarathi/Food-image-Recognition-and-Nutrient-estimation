import os
from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import tkinter as tk

# import your ViewData class (contains 4 buttons)
from dataupload import ViewData


def act():
    username = admin_var.get()
    pwd = pass_var.get()

    if username == "Admin" and pwd == "Admin":
        messagebox.showinfo("Success", "Login Successful! Moving to next page...")
        winadmin.destroy()
        ViewData()     # <-- Opens the next window
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


# --------------------------------------------
# LOGIN WINDOW
# --------------------------------------------

winadmin = Tk()
winadmin.title("Food Calorie Estimation")
winadmin.geometry("1100x1000")
winadmin.configure(bg="#34bfbb")

# Background image
image1 = Image.open("background.png")
img = image1.resize((1100, 1000))
test = ImageTk.PhotoImage(img)

label1 = tk.Label(winadmin, image=test)
label1.place(x=0, y=0)

# ❌ Title removed — this line deleted
# Label(winadmin, text='Food Calorie Estimation',
#       bg="#ffb366", font='verdana 15 bold').place(x=120, y=120)

# LABELS
Label(winadmin, text="Admin", bg="#ffffff",
      width=10, font='Verdana 12 bold').place(x=200, y=320)

Label(winadmin, text="Password", bg="#ffffff",
      width=10, font='Verdana 12 bold').place(x=200, y=370)

# ENTRY VARIABLES
admin_var = StringVar()
pass_var = StringVar()

# ENTRIES
Entry(winadmin, width=30, bg="silver",
      textvariable=admin_var).place(x=400, y=320)

Entry(winadmin, width=30, bg="silver",
      show="*", textvariable=pass_var).place(x=400, y=370)

Button(winadmin, text="Login", font='Verdana 12 bold',
       bg="#34bfbb", command=act).place(x=300, y=450)

winadmin.mainloop()
