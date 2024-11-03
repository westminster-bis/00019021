import tkinter as tk
from tkinter import messagebox
import datetime

#Dictionary to store the date
attendance_records = {}

class attendanceapp:
    def __init__(self, root):
        self.root = root
        root.title("Attendance tracker")
        self.root.geometry("600x400")
        self.root.configure(bg="white")
        
        #Start button to enter to the menu
        start_button = tk.Button(root, text="Start attendance tracker", #command=self.open_main_menu,
                                  bg="white", font=("montserrat", 20, "bold"), padx=20, pady=20)
        start_button.pack(padx=5, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = attendanceapp(root)
    root.mainloop()