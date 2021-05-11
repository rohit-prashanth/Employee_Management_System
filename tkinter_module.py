from tkinter import *
from tkinter import messagebox
def home_console():
        root = Tk()
        root.title("Admin Console")
        root.geometry("300x200")
        my_label = Label(root, text="Welcome To Employee Management System!").pack()
        my_label = Label(root, text="Login as:").pack()
        frame = LabelFrame(root , text="ADMIN").pack(padx=10,pady=10)
        emp_creation = Button(frame, text = "ADMIN",command = Adminlogin).pack()
        frame = LabelFrame(root , text="Employee", padx=5, pady=5).pack(padx=10,pady=10)
        list_of_emp = Button(frame, text = "Employee",command=Employeelogin).pack()
        root.mainloop()
def adminvalidation():
        username = user_entry.get()
        password = pass_entry.get()
        if username == 'username' and password == 'password':
            adminconsole()
        else:
            messagebox.showwarning('Login Page', 'The username or password you entered is incorrect')
def employeevalidation():
        username = user_entry.get()
        password = pass_entry.get()
        if username == 'vinod' and password == 'vinod123':
            loginconsole()
        else:
            messagebox.showwarning('Login Page', 'The username or password you entered is incorrect')
def adminconsole():
            root = Tk()
            root.title("Admin Console")
            button = Button(root, text = 'Create Employee Account')
            button.grid(row=2, column=0, columnspan=2)
            button = Button(root, text = 'List Employee Details')
            button.grid(row=4, column=0, columnspan=2)
            button = Button(root, text = 'Employee Leave Requests')
            button.grid(row=6, column=0, columnspan=2)
            button = Button(root, text = 'Account Deletion')
            button.grid(row=8, column=0, columnspan=2)
            root.mainloop()
def loginconsole():
            root = Tk()
            root.title("employee Console")
            button = Button(root, text = 'search for employee',command="")
            button.grid(row=2, column=0, columnspan=2)
            button = Button(root, text = 'leave request',command="")
            button.grid(row=4, column=0, columnspan=2)
            button = Button(root, text = 'change password ',command="")
            button.grid(row=6, column=0, columnspan=2)
            root.mainloop()
        
def Adminlogin():
    global user_entry,pass_entry
    root = Tk(className = 'Admin Login')
    Label(root, text='Username').grid(row=0)
    Label(root, text='Password').grid(row=1)
    user_entry = Entry(root)
    pass_entry = Entry(root)
    user_entry.grid(row=0, column=1)
    pass_entry.grid(row=1, column=1)
    button = Button(root, text = 'submit',command=adminvalidation)
    button.grid(row=2, column=0, columnspan=2)
    root.mainloop()
def Employeelogin():
    global user_entry,pass_entry
    root = Tk(className = 'Employee Login')
    Label(root, text='Username').grid(row=0)
    Label(root, text='Password').grid(row=1)
    user_entry = Entry(root)
    pass_entry = Entry(root)
    user_entry.grid(row=0, column=1)
    pass_entry.grid(row=1, column=1)
    button = Button(root, text = 'submit',command=employeevalidation)
    button.grid(row=2, column=0, columnspan=2)
    root.mainloop()
home_console()
