import tkinter as tk
from tkinter import messagebox

def check_login():
    username = username_entry.get()
    if not username:
        messagebox.showwarning("Please, enter the username")
    elif username == "admin":
        messagebox.showinfo("Welcome admin")
    else:
        messagebox.showerror("Access denied")

root = tk.Tk()
root.title("Login Window")

tk.Label(root, text="Enter Username:").pack(pady=10)
username_entry=tk.Entry(root)
username_entry.pack(pady=10)

login_button=tk.Button(root, text="Log in", command=check_login)
login_button.pack(pady=10)

root.mainloop()

