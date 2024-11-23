from tkinter import *
from tkinter import messagebox

class Report:
    def __init__(self, root, connection):
        self.root = root
        self.connection = connection
        self.root.title("Result")
        self.root.geometry("1200x380")
        self.root.resizable(False, False)
        self.root.focus_force()

        # Variables
        self.search_value = IntVar()

        title = Label(self.root, text = "View Student Results", font = ('Goudy old style', 20, 'bold'), bg = '#033054', fg = 'white').place(x = 10, y = 15, width = 1180, height = 40)

        search_lbl = Label(self.root, text = 'Search|Roll no.', font = ('Goudy old style', 20, 'bold')).place(x = 250, y = 70)
        txt_search = Entry(self.root, font = ('Goudy old style', 20, 'bold'), bg = 'lightyellow', bd = 2, textvariable = self.search_value).place(x = 450, y = 70, width = 300)
        search_btn = Button(self.root, text = 'Search', cursor = 'hand2', bg = 'lightgrey', fg = 'black', font = ('Goudy old style', 20, 'bold'), command = self.search).place(x = 790, y = 70, height = 40, width = 120)

        roll_lbl = Label(self.root, text = 'Roll No.', font = ('Goudy old style', 15), relief = GROOVE, bd = 2).place(x = 100, y = 150, width = 150, height = 50)
        name_lbl = Label(self.root, text = 'Name', font = ('Goudy old style', 15), relief = GROOVE, bd = 2).place(x = 250, y = 150, width = 200, height = 50)
        course_lbl = Label(self.root, text = 'Course', font = ('Goudy old style', 15), relief = GROOVE, bd = 2).place(x = 450, y = 150, width = 150, height = 50)
        marks_obt_lbl = Label(self.root, text = 'Marks Obtained', font = ('Goudy old style', 15), relief = GROOVE, bd = 2).place(x = 600, y = 150, width = 250, height = 50)
        max_marks_lbl = Label(self.root, text = 'Maximum Marks', font = ('Goudy old style', 15), relief = GROOVE, bd = 2).place(x = 850, y = 150, width = 250, height = 50)

        self.roll_lbl = Label(self.root, font = ('Goudy old style', 15), relief = GROOVE, bd = 2)
        self.roll_lbl.place(x = 100, y = 200, width = 150, height = 50)
        self.name_lbl = Label(self.root, font = ('Goudy old style', 15), relief = GROOVE, bd = 2)
        self.name_lbl.place(x = 250, y = 200, width = 200, height = 50)
        self.course_lbl = Label(self.root, font = ('Goudy old style', 15), relief = GROOVE, bd = 2)
        self.course_lbl.place(x = 450, y = 200, width = 150, height = 50)
        self.marks_obt_lbl = Label(self.root, font = ('Goudy old style', 15), relief = GROOVE, bd = 2)
        self.marks_obt_lbl.place(x = 600, y = 200, width = 250, height = 50)
        self.max_marks_lbl = Label(self.root, font = ('Goudy old style', 15), relief = GROOVE, bd = 2)
        self.max_marks_lbl.place(x = 850, y = 200, width = 250, height = 50)

        btn_done = Button(self.root, text = 'Done', font = ('goudy old style', 20, 'bold'), bg = 'lightblue', fg = 'black', cursor = 'hand2', command = self.exit).place(x = 540, y = 300, width = 120, height = 40)

    def search(self):
        if self.search_value.get() == 0:
            messagebox.showerror("Error", "Please enter a roll number.", parent = self.root)
        else:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM results WHERE roll_no = %s", (self.search_value.get(),))
            row = cursor.fetchone()
            if row is None:
                messagebox.showinfo("Info", "Student not found.", parent = self.root)
            else:
                self.roll_lbl.config(text = row[1])
                self.name_lbl.config(text = row[2])
                self.course_lbl.config(text = row[3])
                self.marks_obt_lbl.config(text = row[4])
                self.max_marks_lbl.config(text = row[5])

    def exit(self):
        self.root.destroy()
