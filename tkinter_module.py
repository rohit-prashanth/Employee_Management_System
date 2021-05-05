# -*- coding: utf-8 -*-
"""
Created on Tue May  4 21:33:29 2021

@author: rohit
"""
from tkinter import *


class Tkinter:
    
    def adminconsole_tkinter(self):
        self.root = Tk()
        self.root.title("Admin Console")
        self.root.geometry("400x300")
        
        self.my_label = Label(self.root, text="Welcome To Admin Console!").pack()
        
        self.frame = LabelFrame(self.root , text="Create Employee Account").pack(padx=10,pady=10)
        self.emp_creation = Button(self.frame, text = "Create Employee Account").pack()
        
        self.frame = LabelFrame(self.root , text="List Employee Details", padx=5, pady=5).pack(padx=10,pady=10)
        self.list_of_emp = Button(self.frame, text = "List Employee Details").pack()
        
        self.frame = LabelFrame(self.root , text="Employee Leave Requests", padx=5, pady=5).pack(padx=10,pady=10)
        self.leave_requests = Button(self.frame, text = "Employee Leave Requests").pack()
        
        self.frame = LabelFrame(self.root , text="Account Deletion", padx=5, pady=5).pack(padx=10,pady=10)
        self.account_deletion = Button(self.frame, text = "Account Deletion").pack()
        
        self.root.mainloop()
        
        
obj = Tkinter()

obj.adminconsole_tkinter()