from tkinter import *
from tkinter import ttk, messagebox

class Student:
    def __init__(self, root, connection):
        self.root = root
        self.connection = connection
        self.root.title("Student")
        self.root.geometry("1200x480")
        self.root.resizable(False, False)
        self.root.focus_force()

        # Variables
        self.rollno = IntVar()
        self.name = StringVar()
        self.email = StringVar()
        self.gender = StringVar()
        self.state = StringVar()
        self.dob = StringVar()
        self.contact = StringVar()
        self.admission_date = StringVar()
        self.course = StringVar()
        self.city = StringVar()
        self.pin = IntVar()
        self.search_value = StringVar()


        title = Label(self.root, text = "Manage Student Details", font = ('Goudy old style', 20, 'bold'), bg = '#033054', fg = 'white').place(x = 10, y = 15, width = 1180, height = 35)

        lbl_rollno = Label(self.root, text = "Roll No.", font = ('Goudy old style', 15, 'bold')).place(x = 10, y = 60)
        lbl_name = Label(self.root, text = "Name", font = ('Goudy old style', 15, 'bold')).place(x = 10, y = 100)
        lbl_email = Label(self.root, text = "Email", font = ('Goudy old style', 15, 'bold')).place(x = 10, y = 140)
        lbl_gender = Label(self.root, text = "Gender", font = ('Goudy old style', 15, 'bold')).place(x = 10, y = 180)
        lbl_state = Label(self.root, text = "State", font = ('Goudy old style', 15, 'bold')).place(x = 10, y = 220)
        lbl_address = Label(self.root, text = "Address", font = ('Goudy old style', 15, 'bold')).place(x = 10, y = 260)
        lbl_dob = Label(self.root, text = 'D.O.B.', font = ('Goudy old style', 15, 'bold')).place(x = 370, y = 60)
        lbl_contact = Label(self.root, text = 'Contact', font = ('Goudy old style', 15, 'bold')).place(x = 370, y = 100)
        lbl_admission = Label(self.root, text = 'Adm. Date', font = ('Goudy old style', 15, 'bold')).place(x = 370, y = 140)
        lbl_course = Label(self.root, text = 'Course', font = ('Goudy old style', 15, 'bold')).place(x = 370, y = 180)
        lbl_city = Label(self.root, text = 'City', font = ('Goudy old style', 15, 'bold')).place(x = 310, y = 220)
        lbl_pin = Label(self.root, text = 'Pin', font = ('Goudy old style', 15, 'bold')).place(x = 520, y = 220)
        lbl_search = Label(self.root, text = 'Search|Name', font = ('Goudy old style', 15, 'bold')).place(x = 750, y = 60)

        self.course_list = []
        self.getCourseList()

        self.txt_rollno = Entry(self.root, font = ('Goudy old style', 15,'bold'), bg = 'lightyellow', textvariable = self.rollno)
        self.txt_rollno.place(x = 150, y = 60, width = 200)
        txt_name = Entry(self.root, font = ('Goudy old style', 15, 'bold'), bg = 'lightyellow', textvariable = self.name).place(x = 150, y = 100, width = 200)
        txt_email = Entry(self.root, font = ('Goudy old style', 15, 'bold'), bg = 'lightyellow', textvariable = self.email).place(x = 150, y = 140, width = 200)
        self.txt_gender = ttk.Combobox(self.root, font = ('Goudy old style', 15, 'bold'), values = ['Male', 'Female', 'Other'], state = 'readonly', justify = CENTER, textvariable = self.gender)
        self.txt_gender.place(x = 150, y = 180, width = 200)
        self.txt_gender.set("Select")
        txt_state = Entry(self.root, font = ('Goudy old style', 15, 'bold'), bg = 'lightyellow', textvariable = self.state).place(x = 150, y = 220, width = 150)
        self.txt_address = Text(self.root, font = ('Goudy old style', 15, 'bold'), bg = 'lightyellow')
        self.txt_address.place(x = 150, y = 260, height = 100, width = 550)
        txt_dob = Entry(self.root, font = ('Goudy old style', 15, 'bold'), bg = 'lightyellow', textvariable = self.dob).place(x = 500, y = 60, width = 200)
        txt_contact = Entry(self.root, font = ('Goudy old style', 15, 'bold'), bg = 'lightyellow', textvariable = self.contact).place(x = 500, y = 100, width = 200)
        txt_admission = Entry(self.root, font = ('Goudy old style', 15, 'bold'), bg = 'lightyellow', textvariable = self.admission_date).place(x = 500, y = 140, width = 200)
        self.txt_course = ttk.Combobox(self.root, font = ('Goudy old style', 15, 'bold'), values = self.course_list, state = 'readonly', justify = CENTER, textvariable = self.course)
        self.txt_course.place(x = 500, y = 180, width = 200)
        self.txt_course.set('Empty')
        txt_city = Entry(self.root, font = ('Goudy old style', 15, 'bold'), bg = 'lightyellow', textvariable = self.city).place(x = 360, y = 220, width = 150)
        txt_pin = Entry(self.root, font = ('Goudy old style', 15, 'bold'), bg = 'lightyellow', textvariable = self.pin).place(x = 570, y = 220, width = 130)
        txt_search = Entry(self.root, font = ('Goudy old style', 15, 'bold'), bg = 'lightyellow', textvariable = self.search_value).place(x = 900, y = 60, width = 150)

        btn_add = Button(self.root, text = 'ADD', font = ('Goudy old style', 15, 'bold'), bg = '#2196f3', fg = 'white', bd = 5, cursor = 'hand2', command = self.add).place(x = 150, y = 400, width = 110, height = 40)
        btn_upd = Button(self.root, text = 'UPDATE', font = ('Goudy old style', 15, 'bold'), bg = '#4caf50', fg = 'white', bd = 5, cursor = 'hand2', command = self.update).place(x = 270, y = 400, width = 110, height = 40)
        btn_del = Button(self.root, text = 'DELETE', font = ('Goudy old style', 15, 'bold'), bg = '#f44336', fg = 'white', bd = 5, cursor = 'hand2', command = self.delete).place(x = 390, y = 400, width = 110, height = 40)
        btn_clear = Button(self.root, text = 'CLEAR', font = ('Goudy old style', 15, 'bold'), bg = '#607d8b', fg = 'white', bd = 5, cursor = 'hand2', command = self.clear).place(x = 510, y = 400, width = 110, height = 40)
        btn_search = Button(self.root, text = 'Search', font = ('Goudy old style', 15, 'bold'), bg = 'lightgrey', fg = 'black', bd = 5, cursor = 'hand2', command = self.search).place(x = 1060, y = 55, width = 120, height = 38)

        self.S_frame = Frame(self.root, relief=RIDGE, bd = 2)
        self.S_frame.place(x = 710, y = 100, width  = 460, height = 340)

        scrolly = Scrollbar(self.S_frame, orient = VERTICAL)
        scrollx = Scrollbar(self.S_frame, orient = HORIZONTAL)

        self.student_table = ttk.Treeview(self.S_frame, columns = ('sid', 'name', 'email', 'gender', 'state', 'address', 'dob', 'contact', 'admission', 'course', 'city', 'pin'), xscrollcommand = scrollx.set, yscrollcommand = scrolly.set )
        scrollx.pack(side = BOTTOM, fill = X)
        scrolly.pack(side = RIGHT, fill = Y)
        scrollx.config(command = self.student_table.xview)
        scrolly.config(command = self.student_table.yview)
        self.student_table.heading('sid', text = 'Roll No')
        self.student_table.heading('name', text = 'Name')
        self.student_table.heading('email', text = 'Email')
        self.student_table.heading('gender', text = 'Gender')
        self.student_table.heading('state', text = 'State')
        self.student_table.heading('address', text = 'Address')
        self.student_table.heading('dob', text = 'DOB')
        self.student_table.heading('contact', text = 'Contact')
        self.student_table.heading('admission', text = 'Admission')
        self.student_table.heading('course', text = 'Course')
        self.student_table.heading('city', text = 'City')
        self.student_table.heading('pin', text = 'Pin')
        self.student_table['show'] = 'headings'
        self.student_table.column('sid', width = 75)
        self.student_table.column('name', width = 150)

        self.student_table.pack(fill = BOTH, expand = True)
        self.student_table.bind("<ButtonRelease-1>", self.get_data)

        self.show()

        self.txt_rollno.config(state = 'readonly')

    def getCourseList(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT name FROM Courses")
        rows = cursor.fetchall()
        for row in rows:
            self.course_list.append(row[0])
        cursor.close()

    def get_data(self, event):
        r = self.student_table.focus()
        content = self.student_table.item(r)
        row = content['values']
        self.rollno.set(row[0])
        self.name.set(row[1])
        self.email.set(row[2])
        self.gender.set(row[3])
        self.state.set(row[4])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END, row[5])
        self.dob.set(row[6])
        self.contact.set(row[7])
        self.admission_date.set(row[8])
        self.course.set(row[9])
        self.city.set(row[10])
        self.pin.set(row[11])

    def add(self):
        if self.name.get() == '' or self.email.get() == '' or self.gender.get() == 'Select' or self.state.get() == '' or self.txt_address.get('1.0', END) == '' or self.dob.get() == '' or self.contact.get() == 0 or self.pin.get() == 0 or self.city.get() == '' or self.admission_date.get() ==  '' or self.course.get() == 'Empty':
            messagebox.showerror('Error', 'All fields are required', parent = self.root)
        elif self.rollno.get() != 0:
            messagebox.showerror('Error', 'Roll No. already exists.', parent = self.root)
        elif len(str(self.pin.get())) != 6:
            messagebox.showerror('Error', 'Pin should be a 6-digit number', parent = self.root)
        elif len(self.contact.get()) != 10:
            messagebox.showerror('Error', 'Contact should be a 10-digit number', parent = self.root)
        else:
            cursor = self.connection.cursor()
            try:
                cursor.execute("INSERT INTO Students (name, email, gender, state, address, dob, contact, adm_date, course, city, pin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", ( self.name.get(), self.email.get(), self.gender.get(), self.state.get(), self.txt_address.get('1.0', END)[:-1], self.dob.get(), self.contact.get(), self.admission_date.get(), self.course.get(), self.city.get(), self.pin.get()))
                self.connection.commit() 
                messagebox.showinfo('Success', 'Student added successfully', parent = self.root)
            except Exception as e:
                messagebox.showerror('Error', str(e), parent = self.root)
            finally:
                cursor.close()
                self.show()

    def update(self):
        if self.rollno.get() == 0:
            messagebox.showerror('Error', 'Select student from list.', parent = self.root)
        else:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Students where roll_no = %s", (self.rollno.get(),))
            row = cursor.fetchone()
            if row:
                try:
                    cursor.execute("UPDATE Students SET name = %s, email = %s, gender = %s, state = %s, address = %s, dob = %s, contact = %s, adm_date = %s, course = %s, city = %s, pin = %s WHERE roll_no = %s", (self.name.get(), self.email.get(), self.gender.get(), self.state.get(), self.txt_address.get('1.0', END)[:-1], self.dob.get(), self.contact.get(), self.admission_date.get(), self.course.get(), self.city.get(), self.pin.get(), self.rollno.get()))
                    self.connection.commit()
                    messagebox.showinfo('Success', 'Student details updated successfully.', parent = self.root)
                    self.show()
                except Exception as e:
                    messagebox.showerror('Error', f'Error due to {e}', parent = self.root)
                finally:
                    cursor.close()
            else:
                messagebox.showerror('Error', 'Student not found.', parent = self.root)
            
            

    def delete(self):
        if self.rollno.get() == 0:
            messagebox.showerror('Error', 'Select student from list.', parent = self.root)
        else:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Students where roll_no = %s", (self.rollno.get(),))
            row = cursor.fetchone()
            if row:
                try:
                    cursor.execute("DELETE FROM Students WHERE roll_no = %s", (self.rollno.get(),))
                    self.connection.commit()
                    messagebox.showinfo('Success', 'Student deleted successfully.', parent = self.root)
                    self.show()
                except Exception as e:
                    messagebox.showerror('Error', f'Error due to {e}', parent = self.root)
                finally:
                    cursor.close()
            else:
                messagebox.showerror('Error', 'Student not found.', parent = self.root)

    def clear(self):
        self.rollno.set(0)
        self.name.set('')
        self.email.set('')
        self.txt_gender.set('Select')
        self.state.set('')
        self.txt_address.delete('1.0', END)
        self.dob.set('')
        self.contact.set('')
        self.admission_date.set('')
        self.txt_course.set('Empty')
        self.city.set('')
        self.pin.set(0)
        self.search_value.set('')
        self.show()

    def search(self):
        cursor = self.connection.cursor()
        search_value = self.search_value.get()
        cursor.execute("SELECT * FROM Students WHERE name = %s", (search_value,))
        row = cursor.fetchone()
        if row == None:
            messagebox.showinfo('Info', 'Student not found.', parent = self.root)
        else:
            self.show(search_value)

    def show(self, name = None):
        cursor = self.connection.cursor()
        try:
            if name == None:
                cursor.execute("SELECT * FROM Students")
                rows = cursor.fetchall()
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert('', END, values = row)
            else:
                cursor.execute("SELECT * FROM Students WHERE name = %s", (name,))
                row = cursor.fetchone()
                self.student_table.delete(*self.student_table.get_children())
                self.student_table.insert('', END, values = row)


        except Exception as e:
            messagebox.showerror('Error', f'Error due to {e}', parent = self.root)
