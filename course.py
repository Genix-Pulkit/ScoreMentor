from tkinter import *
from tkinter import ttk, messagebox

class Course:
    def __init__(self, root, connection):
        self.root = root
        self.connection = connection
        self.root.title("Course")
        self.root.geometry("1200x480")
        self.root.resizable(False, False)
        self.root.focus_force()

        # Text Variables
        self.courseName = StringVar()
        self.duration = StringVar()
        self.fees = IntVar()
        self.search_var = StringVar()

        title = Label(self.root, text = "Manage Course Details", font = ('Goudy old style', 20, 'bold'), bg = '#033054', fg = 'white').place(x = 10, y = 15, width = 1180, height = 35)

        lbl_courseName = Label(self.root, text = "Course Name", font = ('Goudy old style', 15, 'bold')).place(x = 10, y = 60)
        lbl_duration = Label(self.root, text = "Duration", font = ('Goudy old style', 15, 'bold')).place(x = 10, y = 100)
        lbl_fees = Label(self.root, text = "Fees", font = ('Goudy old style', 15, 'bold')).place(x = 10, y = 140)
        lbl_description = Label(self.root, text = "Description", font = ('Goudy old style', 15, 'bold')).place(x = 10, y = 180)

        self.txt_courseName = Entry(self.root, font = ('Goudy old style', 15, 'bold'), bg = 'lightyellow', textvariable = self.courseName)
        self.txt_courseName.place(x = 150, y = 60, width = 200)
        txt_duration = Entry(self.root, font = ('Goudy old style', 15, 'bold'), bg = 'lightyellow', textvariable = self.duration).place(x = 150, y = 100, width = 200)
        txt_fees = Entry(self.root, font = ('Goudy old style', 15, 'bold'), bg = 'lightyellow', textvariable = self.fees).place(x = 150, y = 140, width = 200)
        self.txt_description = Text(self.root, font = ('Goudy old style', 15, 'bold'), bg = 'lightyellow')
        self.txt_description.place(x = 150, y = 180, width = 500, height = 100)

        btn_add = Button(self.root, text = 'ADD', font = ('Goudy old style', 15, 'bold'), bg = '#2196f3', fg = 'white', bd = 5, cursor = 'hand2', command = self.add).place(x = 150, y = 360, width = 110, height = 40)
        btn_upd = Button(self.root, text = 'UPDATE', font = ('Goudy old style', 15, 'bold'), bg = '#4caf50', fg = 'white', bd = 5, cursor = 'hand2', command = self.update).place(x = 270, y = 360, width = 110, height = 40)
        btn_del = Button(self.root, text = 'DELETE', font = ('Goudy old style', 15, 'bold'), bg = '#f44336', fg = 'white', bd = 5, cursor = 'hand2', command = self.delete).place(x = 390, y = 360, width = 110, height = 40)
        btn_clear = Button(self.root, text = 'CLEAR', font = ('Goudy old style', 15, 'bold'), bg = '#607d8b', fg = 'white', bd = 5, cursor = 'hand2', command  = self.clear).place(x = 510, y = 360, width = 110, height = 40)

        lbl_search  = Label(self.root, text = 'Course Name', font = ('Goudy old style', 15, 'bold')).place(x = 670, y = 60)
        txt_search = Entry(self.root, font = ('Goudy old style', 15), bg = 'lightyellow', textvariable = self.search_var).place(x = 800, y = 60, width  = 180)
        btn_search = Button(self.root, text = 'Search', font = ('Goudy old style', 15, 'bold'), cursor = 'hand2', bg = 'lightgrey', fg = 'black', command = self.search).place(x = 1000, y = 60, width = 120, height = 28)

        self.C_frame = Frame(self.root, relief=RIDGE, bd = 2)
        self.C_frame.place(x = 670, y = 100, width  = 500, height = 340)


        self.course_table = ttk.Treeview(self.C_frame, columns = ('cid', 'name', 'duration', 'fees', 'description'))
        self.course_table.heading(column='cid', text = 'ID')
        self.course_table.heading(column='name', text = 'Name')
        self.course_table.heading(column='duration', text = 'Duration')
        self.course_table.heading(column='fees', text = 'Fees')
        self.course_table.heading(column='description', text = 'Description')
        self.course_table['show'] = 'headings'
        self.course_table.column('cid', width = 50)
        self.course_table.column('name', width = 100)
        self.course_table.column('duration', width = 100)
        self.course_table.column('fees', width = 100)
        self.course_table.column('description', width = 140)
        self.course_table.pack(fill = BOTH, expand = 1)
        self.course_table.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    def get_data(self, event):
        self.txt_courseName.config(state = 'readonly')
        r = self.course_table.focus()
        content = self.course_table.item(r)
        row = content['values']
        self.courseName.set(row[1])
        self.duration.set(row[2])
        self.fees.set(row[3])
        self.txt_description.delete('1.0', END)
        self.txt_description.insert(END, row[4])

    def add(self):
        if self.courseName.get() == '' or self.duration.get() == '' or self.fees.get() == 0 or self.txt_description.get('1.0', END) == '':
            messagebox.showerror('Error', 'All Fields are required.', parent = self.root)
        elif self.fees.get() < 0:
            messagebox.showerror('Error', 'Fees cannot be negative.', parent = self.root)
        else:
            cursor = self.connection.cursor()

            courseName = self.courseName.get()
            duration = self.duration.get()
            fees = self.fees.get()  
            description = self.txt_description.get('1.0', END)[:-1]

            cursor.execute("SELECT * FROM Courses WHERE name = %s", (courseName,))
            row = cursor.fetchone()

            if row != None:
                messagebox.showerror('Error', 'Course with this name already exists. Try with different name.', parent = self.root)
            else:
                cursor.execute("INSERT INTO Courses (name, duration, fees, description) VALUES (%s, %s, %s, %s)", (courseName, duration, fees, description))
                self.connection.commit()
                messagebox.showinfo('Success', 'Course added successfully.', parent = self.root)

            self.show()

            cursor.close()


    def update(self):
        if self.courseName.get() == '':
            messagebox.showerror('Error', 'Select course from list.', parent = self.root)
        else:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Courses WHERE name = %s", (self.courseName.get(),))
            row = cursor.fetchone()
            if row == None:
                messagebox.showerror('Error', 'Course not found.', parent = self.root)
            else:
                try:
                    cursor.execute("UPDATE Courses SET duration = %s,fees = %s,description = %s WHERE name = %s", (self.duration.get(), self.fees.get(), self.txt_description.get('1.0', END)[:-1], self.courseName.get()))
                    self.connection.commit()
                    messagebox.showinfo('Success', 'Course updated successfully.', parent = self.root)
                    self.show()
                except Exception as e:
                    messagebox.showerror('Error', f'Error due to {e}', parent = self.root)
                finally:
                    cursor.close()

    def delete(self):
        if self.courseName.get() == '':
            messagebox.showerror('Error', 'Select course from list.', parent = self.root)
        else:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Courses WHERE name = %s", (self.courseName.get(),))
            row = cursor.fetchone()
            if row == None:
                messagebox.showerror('Error', 'Course not found.', parent = self.root)
            else:
                do = messagebox.askyesno('Warning', 'Are you sure you want to delete this course?', parent = self.root)
                if do == True:
                    try:
                        cursor.execute("DELETE FROM Courses WHERE name = %s", (self.courseName.get(),))
                        self.connection.commit()
                        messagebox.showinfo('Success', 'Course deleted successfully.', parent = self.root)
                        self.clear()
                    except Exception as e:
                        messagebox.showerror('Error', f'Error due to {e}', parent = self.root)
                    finally:
                        cursor.close()

                else:
                    return None

    def clear(self):
        self.show()
        self.courseName.set('')
        self.duration.set('')
        self.fees.set(0)
        self.txt_description.delete('1.0', END)
        self.search_var.set('')
        self.txt_courseName.config(state = 'normal')

    def search(self):
        cursor = self.connection.cursor()
        search_value = self.search_var.get()
        cursor.execute("SELECT * FROM Courses WHERE name = %s", (search_value,))
        row = cursor.fetchone()
        if row == None:
            messagebox.showinfo('Info', 'Course not found.', parent = self.root)
        else:
            self.show(search_value)

    def show(self, name = None):
        cursor = self.connection.cursor()

        try:
            if name == None:
                cursor.execute("SELECT * FROM Courses")
                rows = cursor.fetchall()
                self.course_table.delete(*self.course_table.get_children())
                for row in rows:
                    self.course_table.insert('', END, values = row)
            else:
                cursor.execute("SELECT * FROM Courses WHERE name = %s", (name,))
                row = cursor.fetchone()
                self.course_table.delete(*self.course_table.get_children())
                self.course_table.insert('', END, values = row)


        except Exception as e:
            messagebox.showerror('Error', f'Error due to {e}', parent = self.root)
