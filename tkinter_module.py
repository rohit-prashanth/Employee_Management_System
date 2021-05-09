# -*- coding: utf-8 -*-
"""
Created on Tue May  4 21:33:29 2021

@author: rohit
"""
from tkinter import *


class Tkinter:

    def home_console(self):
        self.root = Tk()
        self.root.title("Admin Console")
        self.root.geometry("300x200")
        
        self.my_label = Label(self.root, text="Welcome To Employee Management System!").pack()

        self.my_label = Label(self.root, text="Login as:").pack()
        
        self.frame = LabelFrame(self.root , text="ADMIN").pack(padx=10,pady=10)
        self.emp_creation = Button(self.frame, text = "ADMIN",command = self.admin_signin).pack()
        
        self.frame = LabelFrame(self.root , text="Employee", padx=5, pady=5).pack(padx=10,pady=10)
        self.list_of_emp = Button(self.frame, text = "Employee",command = self.emp_signin ).pack()
        
        self.root.mainloop()

    def emp_signin(self):
        self.root = Tk()
        self.root.title("Employee SignIN")
        self.root.geometry("300x200")
        
        self.my_label = Label(self.root, text="Welcome To Employee Management System!").pack()
        self.my_label = Label(self.root, text="Enter Your Credentials").pack()
        self.my_label = Label(self.root, text="Username:").pack()

        e = Entry(self.root,width = 30).pack()

        self.my_label = Label(self.root, text="Password:").pack()

        e = Entry(self.root,width= 30).pack()

        signin = Button(self.root,text = "Submit").pack()        
        
        self.root.mainloop()

    def admin_signin(self):
        self.root = Tk()
        self.root.title("Admin SignIN")
        self.root.geometry("300x200")
        
        self.my_label = Label(self.root, text="Welcome To Employee Management System!").pack()
        self.my_label = Label(self.root, text="Enter Your Credentials").pack()
        self.my_label = Label(self.root, text="Username:").pack()

        e = Entry(self.root,width = 30).pack()

        self.my_label = Label(self.root, text="Password:").pack()

        e = Entry(self.root,width= 30).pack()

        signin = Button(self.root,text = "Submit").pack()        
        
        self.root.mainloop()


    
    def adminconsole_tkinter(self):
        self.root = Tk()
        self.root.title("Admin Console")
        self.root.geometry("400x300")
        
        self.my_label = Label(self.root, text="Welcome To Admin Console!").pack()
        
        self.frame = LabelFrame(self.root , text="Create Employee Account").pack()
        self.emp_creation = Button(self.frame, text = "Create Employee Account").pack()
        
        self.frame = LabelFrame(self.root , text="List Employee Details").pack()
        self.list_of_emp = Button(self.frame, text = "List Employee Details").pack()
        
        self.frame = LabelFrame(self.root , text="Employee Leave Requests").pack()
        self.leave_requests = Button(self.frame, text = "Employee Leave Requests").pack()
        
        self.frame = LabelFrame(self.root , text="Account Deletion").pack()
        self.account_deletion = Button(self.frame, text = "Account Deletion").pack()
        
        self.root.mainloop()

    def employeeconsole_tkinter(self):
        self.root = Tk()
        self.root.title("Employee Console")
        self.root.geometry("400x300")
        
        self.my_label = Label(self.root, text="Welcome To Employee Console!").pack()
        
        self.frame = LabelFrame(self.root , text="Create Employee Account",padx).pack(padx=10,pady=10)
        self.emp_creation = Button(self.frame, text = "Create Employee Account").pack()
        
        self.frame = LabelFrame(self.root , text="List Employee Details", padx=5, pady=5).pack(padx=10,pady=10)
        self.list_of_emp = Button(self.frame, text = "List Employee Details").pack()
        
        self.frame = LabelFrame(self.root , text="Employee Leave Requests", padx=5, pady=5).pack(padx=10,pady=10)
        self.leave_requests = Button(self.frame, text = "Employee Leave Requests").pack()
        
        self.root.mainloop()
        
        
obj = Tkinter()

obj.adminconsole_tkinter()