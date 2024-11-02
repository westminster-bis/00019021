import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Dictionary to store attendance records, organized by subjects
attendance_records = {}

# Main Application Class
class AttendanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Tracker")
        self.root.geometry("400x200")
        self.root.configure(bg="#f0f0f5")

        # Start Button to open main menu with style updates
        start_button = tk.Button(root, text="Start Attendance Tracker", command=self.open_main_menu,
                                 bg="#4CAF50", fg="white", font=("Arial", 14, "bold"), padx=10, pady=10)
        start_button.pack(pady=20)

    def open_main_menu(self):
        menu_window = tk.Toplevel(self.root)
        menu_window.title("Main Menu")
        menu_window.geometry("300x300")
        menu_window.configure(bg="#f7f7f7")

        # Buttons for each functionality with added padding and font styles
        tk.Button(menu_window, text="Add New Student", command=self.add_student_window,
                  bg="#4CAF50", fg="white", font=("Arial", 12), padx=10, pady=5).pack(pady=10)
        tk.Button(menu_window, text="Record Attendance", command=self.record_attendance_window,
                  bg="#4CAF50", fg="white", font=("Arial", 12), padx=10, pady=5).pack(pady=10)
        tk.Button(menu_window, text="View Attendance", command=self.view_attendance_window,
                  bg="#4CAF50", fg="white", font=("Arial", 12), padx=10, pady=5).pack(pady=10)
        tk.Button(menu_window, text="View Attendance Summary", command=self.view_summary_window,
                  bg="#4CAF50", fg="white", font=("Arial", 12), padx=10, pady=5).pack(pady=10)

    def add_student_window(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add New Student")
        add_window.configure(bg="#f7f7f7")

        tk.Label(add_window, text="Enter Student's Name:", bg="#f7f7f7").pack(pady=5)
        name_entry = tk.Entry(add_window)
        name_entry.pack(pady=5)

        tk.Label(add_window, text="Enter Subject:", bg="#f7f7f7").pack(pady=5)
        subject_entry = tk.Entry(add_window)
        subject_entry.pack(pady=5)

        def add_student():
            student_name = name_entry.get().strip()
            subject = subject_entry.get().strip()
            if student_name and subject:
                if student_name not in attendance_records:
                    attendance_records[student_name] = {}
                if subject not in attendance_records[student_name]:
                    attendance_records[student_name][subject] = []
                    messagebox.showinfo("Success", f"Student {student_name} added for {subject}.")
                    add_window.destroy()
                else:
                    messagebox.showwarning("Duplicate Entry", f"Student {student_name} already exists for {subject}.")
            else:
                messagebox.showwarning("Input Error", "Please enter both name and subject.")

        tk.Button(add_window, text="Add Student", command=add_student,
                  bg="#4CAF50", fg="white").pack(pady=10)

    def record_attendance_window(self):
        record_window = tk.Toplevel(self.root)
        record_window.title("Record Attendance")
        record_window.configure(bg="#f7f7f7")

        tk.Label(record_window, text="Enter Student's Name:", bg="#f7f7f7").pack(pady=5)
        name_entry = tk.Entry(record_window)
        name_entry.pack(pady=5)

        tk.Label(record_window, text="Enter Subject:", bg="#f7f7f7").pack(pady=5)
        subject_entry = tk.Entry(record_window)
        subject_entry.pack(pady=5)

        tk.Label(record_window, text="Enter Date (YYYY-MM-DD):", bg="#f7f7f7").pack(pady=5)
        date_entry = tk.Entry(record_window)
        date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        date_entry.pack(pady=5)

        def record_attendance():
            student_name = name_entry.get().strip()
            subject = subject_entry.get().strip()
            date_attended = date_entry.get().strip()
            if student_name in attendance_records and subject in attendance_records[student_name]:
                attendance_records[student_name][subject].append(date_attended)
                messagebox.showinfo("Success", f"Attendance recorded for {student_name} in {subject} on {date_attended}.")
                record_window.destroy()
            else:
                messagebox.showwarning("Name or Subject Error", "Student name or subject not found.")

        tk.Button(record_window, text="Record Attendance", command=record_attendance,
                  bg="#4CAF50", fg="white").pack(pady=10)

    def view_attendance_window(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("View Attendance")
        view_window.configure(bg="#f7f7f7")

        tk.Label(view_window, text="Enter Student's Name:", bg="#f7f7f7").pack(pady=5)
        name_entry = tk.Entry(view_window)
        name_entry.pack(pady=5)

        tk.Label(view_window, text="Enter Subject:", bg="#f7f7f7").pack(pady=5)
        subject_entry = tk.Entry(view_window)
        subject_entry.pack(pady=5)

        def view_attendance():
            student_name = name_entry.get().strip()
            subject = subject_entry.get().strip()
            if student_name in attendance_records and subject in attendance_records[student_name]:
                attendance_list = "\n".join(attendance_records[student_name][subject]) if attendance_records[student_name][subject] else "No attendance records available."
                messagebox.showinfo(f"Attendance for {student_name} in {subject}", attendance_list)
            else:
                messagebox.showwarning("Name or Subject Error", "Student name or subject not found.")

        tk.Button(view_window, text="View Attendance", command=view_attendance,
                  bg="#4CAF50", fg="white").pack(pady=10)

    def view_summary_window(self):
        summary_window = tk.Toplevel(self.root)
        summary_window.title("Attendance Summary")
        summary_window.configure(bg="#f7f7f7")

        tk.Label(summary_window, text="Enter Total Days for Calculation:", bg="#f7f7f7").pack(pady=5)
        days_entry = tk.Entry(summary_window)
        days_entry.pack(pady=5)

        def view_summary():
            try:
                total_days = int(days_entry.get().strip())
                summary_text = ""
                for student_name, subjects in attendance_records.items():
                    for subject, attendance_dates in subjects.items():
                        attended_days = len(attendance_dates)
                        summary_text += f"{student_name} in {subject}: {attended_days} days attended\n"
                messagebox.showinfo("Attendance Summary", summary_text)
                summary_window.destroy()
            except ValueError:
                messagebox.showwarning("Input Error", "Please enter a valid number of days.")

        tk.Button(summary_window, text="View Summary", command=view_summary,
                  bg="#4CAF50", fg="white").pack(pady=10)


# Run the Attendance Tracker Application
if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceApp(root)
    root.mainloop()
