from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from dashboard import RMS

class Register:
    def __init__(self, root, connection):
        self.root = root
        self.connection = connection
        self.root.title("Register")
        self.root.geometry('1350x700')
        self.root.resizable(False, False)

        # Widgets
        self.bg_register = ImageTk.PhotoImage(file = 'images/bg.png')
        Label(root, image = self.bg_register).place(x=0,y=0,relheight=1,relwidth=1)

        self.register_front_img = ImageTk.PhotoImage(file = 'images/front.png')
        Label(root, image = self.register_front_img).place(x=250, y=150)

        # Register Frame
        frame = Frame(root, bg = 'white')
        frame.place(x = 550, y = 150, width = 550, height = 404)

        Label(frame, text='REGISTER HERE', font = ("times new roman", 20, "bold"), bg = 'white', fg = 'Red').place(x = 45,y = 25)

        self.usr_var = StringVar()
        Label(frame, text='Username', font=('times new roman', 15, 'bold'), bg = 'white', fg = 'gray').place(x = 45, y = 65)
        Entry(frame, font=('times new roman', 15), bg = 'lightgray', textvariable= self.usr_var).place(x = 45, y = 95, width=250)

        self.age_var = IntVar()
        Label(frame, text='Age', font=('times new roman', 15, 'bold'), bg = 'white', fg = 'gray').place(x = 325, y = 65)
        Entry(frame, font=('times new roman', 15), bg = 'lightgray', textvariable= self.age_var).place(x = 325, y = 95, width=170)

        self.email_var = StringVar()
        Label(frame, text='Email Address', font=('times new roman', 15, 'bold'), bg = 'white', fg = 'gray').place(x = 45, y = 120)
        Entry(frame, font=('times new roman', 15), bg = 'lightgray', textvariable= self.email_var).place(x = 45, y = 150, width=250)

        self.pass_var = StringVar()
        Label(frame, text='Password', font=('times new roman', 15, 'bold'), bg = 'white', fg = 'gray').place(x = 45, y = 175)
        Entry(frame, font=('times new roman', 15), bg = 'lightgray', textvariable= self.pass_var).place(x = 45, y = 205, width=250)

        self.con_pass_var = StringVar()
        Label(frame, text='Confirm Password', font=('times new roman', 15, 'bold'), bg = 'white', fg = 'gray').place(x = 45, y = 230)
        Entry(frame, font=('times new roman', 15), bg = 'lightgray',  textvariable=self.con_pass_var).place(x = 45, y = 260, width=250)

        self.chk_var = IntVar()
        Checkbutton(frame, text = 'I Agree to the Terms & Conditions', bg = 'white', font = ('times new roman', 12), onvalue = 1, offvalue = 0, variable= self.chk_var).place(x = 45, y = 300)

        Button(frame, text = 'Register Now ->', justify='center', font = ('times new roman', 15, 'bold'), bg = 'green', fg = 'white', command = self.register_data).place(x = 45, y = 340, width = 200)

        Button(root, text = 'Sign In', justify='center', font = ('times new roman', 15, 'bold'), bg = 'white', command = self.sign_in).place(x = 300, y = 460, width = 200)

    def clear(self):
        self.usr_var.set('')
        self.age_var.set(0)
        self.email_var.set('')
        self.pass_var.set('')
        self.con_pass_var.set('')
        self.chk_var.set(0)

    def register_data(self):
        cursor = self.connection.cursor()
        if self.usr_var.get() == '' or self.age_var.get() == 0 or self.con_pass_var.get() == '' or self.email_var.get() == '' or self.pass_var.get() == '':
            messagebox.showerror("Error", "All Fields are Required", parent = self.root)
        elif self.pass_var.get() != self.con_pass_var.get():
            messagebox.showerror("Error", "Password and Confirm Password do not match.", parent = self.root)
        elif self.age_var.get() < 18:
            messagebox.showerror("Error", "You must be at least 18 years old.", parent = self.root)
        elif self.chk_var.get() == 0:
            messagebox.showerror("Error", "Please agree to the Terms & Conditions", parent = self.root)
        else:
            username = self.usr_var.get()
            age = self.age_var.get()
            email = self.email_var.get()
            password = self.pass_var.get()
            try:
                cursor.execute("SELECT * FROM Users WHERE email = %s", (self.email_var.get(),))
                row = cursor.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Email already exists. Please try with another email.", parent = self.root)
                else:
                    cursor.execute("INSERT INTO Users (username, password, email, age) VALUES (%s, %s, %s, %s)", (username, password, email, age))
                    self.connection.commit()
                    cursor.close()
                    messagebox.showinfo("Success", "Registered Successfully", parent = self.root)
                    self.clear()
            except Exception as e:
                messagebox.showerror("Error", f"Error registering user: {e}", parent = self.root)

    def sign_in(self):
        self.root.destroy()
        new_root = Tk()
        obj = SignIn(new_root, self.connection)
        new_root.mainloop()

class SignIn:
    def __init__(self, root, connection):
        self.root = root
        self.connection = connection
        self.root.title("Sign In")
        self.root.geometry('1350x700')
        self.root.resizable(False, False)
        self.bg_login_img = ImageTk.PhotoImage(file = 'images/bg_login.png')
        Label(root, image = self.bg_login_img).place(x = 0, y = 0, relheight=1,relwidth=1)
        self.front_img = ImageTk.PhotoImage(file = 'images/login_front.png')
        Label(root, image=self.front_img).place(x = 250,  y = 150)
        frame = Frame(root, bg = 'white')
        frame.place(x = 550, y = 150 ,width = 550, height=403)
        Label(frame, text='LOGIN HERE', font = ("times new roman", 20, "bold"), bg = 'white', fg = 'Red').place(x = 45,y = 25)
        self.email_login_var = StringVar()
        Label(frame, text='Email Address', font=('times new roman', 15, 'bold'), bg = 'white', fg = 'gray').place(x = 45, y = 85)
        Entry(frame, font=('times new roman', 15), bg = 'lightgray', textvariable= self.email_login_var).place(x = 45, y = 115, width=250)
        self.usr_login_var = StringVar()
        Label(frame, text='Username', font=('times new roman', 15, 'bold'), bg = 'white', fg = 'gray').place(x = 45, y = 145)
        Entry(frame, font=('times new roman', 15), bg = 'lightgray', textvariable= self.usr_login_var).place(x = 45, y = 180, width=250)
        self.pass_login_var = StringVar()
        Label(frame, text='Password', font=('times new roman', 15, 'bold'), bg = 'white', fg = 'gray').place(x = 45, y = 210)
        Entry(frame, font=('times new roman', 15), bg = 'lightgray', textvariable= self.pass_login_var).place(x = 45, y = 240, width=250)
        Button(frame, text = 'Not a member? Sign Up', bg = 'white', fg = 'Green', font = ('times new roman', 15, 'bold'), bd = 0, command = self.register).place(x = 43, y = 270)
        Button(frame, text = 'Login', justify='center', font = ('times new roman', 15, 'bold'), bg = 'green', fg = 'white', command = self.login).place(x = 45, y = 320, width = 200)

    def login(self):
        cursor = self.connection.cursor()
        if self.usr_login_var.get() == '' or self.email_login_var.get() == '' or self.pass_login_var.get() == '':
            messagebox.showerror("Error", "All Fields are Required", parent = self.root)
        else:
            email = self.email_login_var.get()
            username = self.usr_login_var.get()
            password = self.pass_login_var.get()
            try:
                cursor.execute("SELECT * FROM Users WHERE email = %s AND username = %s AND password = %s", (email, username, password))
                row = cursor.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Email, Username or Password", parent = self.root)
                else:
                    messagebox.showinfo("Success", "Logged In Successfully", parent = self.root)
                    self.root.destroy()
                    new_root = Tk()
                    obj = RMS(new_root, self.connection)
                    new_root.mainloop()
            except Exception as e:
                messagebox.showerror("Error", f"Error logging in: {e}", parent = self.root)

    def register(self):
        self.root.destroy()
        new_root = Tk()
        obj = Register(new_root, self.connection)
        new_root.mainloop()