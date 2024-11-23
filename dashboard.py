from tkinter import *
from tkinter import messagebox
from course import Course
from student import Student
from result import Result
from report import Report
import os
import sys

class RMS:
    def __init__(self, root, connection):
        self.root = root
        self.connection = connection
        self.root.title("Student Result Management System")
        self.root.geometry("1600x900")
        self.root.resizable(False, False)

        title = Label(self.root, text = "Score Mentor", font = ('Goudy old style', 20, 'bold'), bg = '#033054', fg = 'white').place(x = 0, y = 0, relwidth = 1, height = 70)

        # Menu
        M_Frame = LabelFrame(self.root, text = 'Menu', font = ('Goudy old style', 15), bg = 'white').place(x = 20, y = 90, width = 1560, height = 120)
        btn_course = Button(self.root, text = 'Course', font = ('Goudy old style', 20, 'bold'), bg = '#0b5377', fg = 'white', cursor = 'hand2', bd = 5, command = self.course). place(x = 40, y = 125, width = 220, height = 60)
        btn_student = Button(self.root, text = 'Student', font = ('Goudy old style', 20, 'bold'), bg = '#0b5377', fg = 'white', cursor = 'hand2', bd = 5, command = self.student).place(x = 290, y = 125, width = 220, height = 60)
        btn_result = Button(self.root, text = 'Result', font = ('Goudy old style', 20, 'bold'), bg = '#0b5377', fg = 'white', cursor = 'hand2', bd = 5, command = self.result).place(x = 540, y = 125, width = 220, height = 60)
        btn_view_result = Button(self.root, text = 'View Result', font =('Goudy old style', 20, 'bold'), bg = '#0b5377', fg = 'white', cursor = 'hand2', bd = 5, command = self.view_result).place(x = 790, y = 125, width = 250, height = 60)
        btn_logout = Button(self.root, text = 'Logout', font = ('Goudy old style', 20, 'bold'), bg = '#0b5377', fg = 'white', cursor = 'hand2', bd = 5, command = self.logout).place(x =1070, y = 125, width = 220, height = 60)
        btn_exit = Button(self.root, text = 'Exit', font = ('Goudy old style', 20, 'bold'), bg = '#0b5377', fg = 'white', cursor = 'hand2', bd = 5, command = self.exit).place(x = 1320, y = 125, width = 230, height = 60)

        # Details
        self.lbl_courses = Label(self.root, text = 'Total Courses\n[ 0 ]', font = ('Goudy old style', 20), bg = '#e43b06', fg = 'white', relief = RIDGE, bd = 10)
        self.lbl_courses.place(x = 20, y = 250, width = 300, height = 150)

        self.lbl_students = Label(self.root, text = 'Total Students\n[ 0 ]', font = ('Goudy old style', 20), bg = '#0676ad', fg = 'white', relief = RIDGE, bd = 10)
        self.lbl_students.place(x = 20, y = 430, width = 300, height = 150)

        self.lbl_results = Label(self.root, text = 'Total Results\n[ 0 ]', font = ('Goudy old style', 20), bg = '#038074', fg = 'white', relief = RIDGE, bd = 10)
        self.lbl_results.place(x = 20, y = 610, width = 300, height = 150)

        footer = Label(self.root, text = 'Student Result Management System\nContact Us for any Technical Issues 60245xxxxx', font = ('GoudyGoudy old style', 12), bg = "#262626", fg = 'white').pack(side = BOTTOM, fill = X)

        frame_welcome = Frame(self.root, relief = RIDGE, bd = 10).place(x = 340, y = 250, width = 1220, height = 510)

        title = Label(self.root, text = '🎉 Welcome to Score Mentor 🎉', font = ('Goudy old style', 40,  'bold')).place(x = 590, y = 280)

        text1 = Label(self.root, text = 'Your comprehensive solution for managing and tracking student results with precision and ease.', font = ('Goudy old style', 20)).place(x = 450, y = 380)

        text2 = Label(self.root, text = "Designed with both teachers and administrators in mind, Score Mentor offers a user-friendly\nplatform to record, update, and retrieve student grades effortlessly. Whether you're managing\nindividual assessments or generating complete reports, Score Mentor ensures quick access to\naccurate data, saving you time and improving efficiency.", font = ('Goudy old style', 20)).place(x = 463, y = 430)

        text3 = Label(self.root, text = "Let’s streamline your grading process and make student performance management easier than\never! Get started now to experience seamless result tracking at your fingertips!", font = ('Goudy old style', 20)).place(x = 455, y = 580)

        self.update()

    def update(self):
        cursor = self.connection.cursor()
        try:

            cursor.execute("SELECT * FROM courses")
            rows = cursor.fetchall()
            self.lbl_courses.config(text = f'Total Courses\n[{len(rows)}]')

            cursor.execute("SELECT * FROM students")
            rows = cursor.fetchall()
            self.lbl_students.config(text = f'Total Students\n[{len(rows)}]')

            cursor.execute("SELECT * FROM results")
            rows = cursor.fetchall()
            self.lbl_results.config(text = f'Total Results\n[{len(rows)}]')

            self.lbl_courses.after(200, self.update)

        except Exception as e:
            messagebox.showerror("Error", f"The error '{e}' occurred.")

    def course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Course(self.new_win, self.connection)

    def student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Student(self.new_win, self.connection)

    def result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Result(self.new_win, self.connection)

    def view_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Report(self.new_win, self.connection)

    def logout(self):
        self.root.destroy()
        os.system("python reg_login.py")

    def exit(self):
        self.root.destroy()
        sys.exit(0)
