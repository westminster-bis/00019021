import tkinter as tk
from tkinter import messagebox
import datetime

# Dictionary to store the date
attendance_records = {}

class attendanceapp:
    def __init__(self, root):
        self.root = root
        root.title("Attendance tracker")
        self.root.geometry("600x400")
        self.root.configure(bg="white")

        # Setting adjustable window
        center_frame = tk.Frame(self.root, bg="lightgrey")
        center_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        #Start button to enter the menu
        start_button = tk.Button(center_frame, text="Start attendance tracker", command=self.open_main_menu,
                                  bg="white", font=("montserrat", 20, "bold"), bd=5, relief="raised")
        start_button.grid(row=0, column=0)

        # Window will not be resized smaller then button
        self.root.update_idletasks()
        self.root.minsize(start_button.winfo_width() + 50, start_button.winfo_height() + 50)

        # Background transition
        start_button.bind("<Enter>", self.on_hover)
        start_button.bind("<Leave>", self.not_hover)

    def on_hover(self, e):
        e.widget["bg"] = "darkgreen"  # Gets green when on hover
    def not_hover(self, e):
        e.widget["bg"] = "white"      # Returns to inital color


        # Main manu
    def open_main_menu(self):
        main_window = tk.Toplevel(self.root)
        main_window.title("Main menu")
        main_window.geometry("500x700")
        main_window.config(bg="aquablue")


if __name__ == "__main__":
    root = tk.Tk()
    app = attendanceapp(root)
    root.mainloop()