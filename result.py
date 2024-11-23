from tkinter import *
from tkinter import ttk, messagebox

class Result:
    def __init__(self, root, connection):
        self.root = root
        self.connection = connection
        self.root.title("Result")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.focus_force()

        # Variables
        self.stdroll = StringVar()
        self.name = StringVar()
        self.course = StringVar()
        self.max_marks = IntVar()
        self.marks_obt = IntVar()

        title = Label(self.root, text = "Add Student Results", font = ('Goudy old style', 20, 'bold'), bg = '#033054', fg = 'white').place(x = 10, y = 15, width = 780, height = 40)

        student_lbl = Label(self.root, text = "Select Student", font = ('Goudy old style', 20, 'bold')).place(x = 60, y = 100)
        name_lbl = Label(self.root, text = "Name", font = ('Goudy old style', '20', 'bold')).place(x = 60, y = 150)
        course_lbl = Label(self.root, text = "Course", font = ('Goudy old style', 20, 'bold')).place(x = 60, y = 200)           
        max_marks_lbl = Label(self.root, text = "Maximum Marks", font = ('Goudy old style', 20, 'bold')).place(x = 60, y = 250)
        marks_obt_lbl = Label(self.root, text = "Marks Obtained", font = ('Goudy old style', 20, 'bold')).place(x = 60, y = 300)

        self.std_list = []
        self.fetch_students()
        self.txt_stdroll = ttk.Combobox(self.root, font = ('Goudy old style', 20, 'bold'), values = self.std_list, state = 'readonly', justify = CENTER, textvariable = self.stdroll)
        self.txt_stdroll.place(x = 300, y = 100, width = 250)
        self.txt_stdroll.set('Select')
        txt_name = Entry(self.root, font = ('Goudy old style', 20, 'bold'), bg = 'lightyellow', state = 'readonly', textvariable = self.name).place(x = 300, y = 150, width = 400)
        txt_course = Entry(self.root, font = ('Goudy old style', 20, 'bold'), bg = 'lightyellow', state = 'readonly', textvariable = self.course).place(x = 300, y = 200, width = 400)
        txt_max_marks = Entry(self.root, font = ('Goudy old style', 20, 'bold'), bg = 'lightyellow', textvariable = self.max_marks).place(x = 300, y = 250, width = 400)
        txt_marks_obt = Entry(self.root, font = ('Goudy old style', 20, 'bold'), bg = 'lightyellow', textvariable = self.marks_obt).place(x = 300, y = 300, width = 400)

        btn_search = Button(self.root, text = "Search",  font = ('Goudy old style', 15, 'bold'), bg = 'lightblue', fg = 'black', cursor = 'hand2', command = self.search).place(x = 570, y = 100, width = 130, height = 40)
        btn_add = Button(self.root, text = 'ADD', font = ('Goudy old style', 20, 'bold'), bg = '#2196f3', fg = 'white', bd = 5, cursor = 'hand2', command = self.add_result).place(x = 150, y = 400, width = 200, height = 80)
        btn_clear = Button(self.root, text = 'CLEAR', font = ('Goudy old style', 20, 'bold'), bg = '#607d8b', fg = 'white', bd = 5, cursor = 'hand2', command = self.clear).place(x = 400, y = 400, width = 200, height = 80)

    def fetch_students(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT roll_no, name FROM students")
        rows = cursor.fetchall()
        for row in rows:
            self.std_list.append(row[0])

    def search(self):
        if self.stdroll.get() == 'Select':
            messagebox.showerror('Error', 'Select student from list.', parent = self.root)
        else:
            cursor = self.connection.cursor()
            cursor.execute("SELECT name, course FROM students WHERE roll_no = %s", (int(self.stdroll.get()),))
            row = cursor.fetchone()
            if row:
                self.name.set(row[0])
                self.course.set(row[1])                
            else:
                messagebox.showinfo('Info', 'Student not found.', parent = self.root)

    def clear(self):
        self.txt_stdroll.set('Select')
        self.name.set('')
        self.course.set('')
        self.max_marks.set(0)
        self.marks_obt.set(0)

    def add_result(self):
        if self.stdroll.get() == 'Select' or self.max_marks.get() == 0 or self.marks_obt.get() == 0:
            messagebox.showerror('Error', 'All fields are required.', parent = self.root)
        else:
            try:
                cursor = self.connection.cursor()
                cursor.execute("INSERT INTO Results (roll_no, name, course, max_marks, marks_obt) VALUES (%s, %s, %s, %s, %s)", (int(self.stdroll.get()), self.name.get(), self.course.get(), self.max_marks.get(), self.marks_obt.get()))
                self.connection.commit()
                messagebox.showinfo('Success', 'Result added successfully.', parent = self.root)
            except Exception as e:
                messagebox.showerror('Error', f'Error due to {e}', parent = self.root)
            finally:
                cursor.close()
