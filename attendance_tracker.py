import tkinter as tk
from tkinter import messagebox
import datetime

#Dictionary to store the date
attendance_records=()

class attendanceapp:
    def __init__(self, root):
        self.root=root
        self.root.titile("Attendance tracker")
        self.root.geometry("600x400")
        self.root.configure(bg="white")
        
