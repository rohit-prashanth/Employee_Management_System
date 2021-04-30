#from database import database
class adminconsole:
    def create_emp_account(self):
        self.f_name=input("enter first name")
        self.l_name=input("enter last name")
        self.username=input("create user name")
        self.email_id=input("enter email address")
        self.password=input("enter password")
        self.emp_salary=float(input("enter employee salary"))
        self.emp_pf_no=input("enter pf no")
        self.join_date=input("enter joining date")
        self.pan_id=input("ener pancard number")
        self.leave_balance=int(input("enter leave balance days"))
        dic={"f_name":self.f_name,"l_name":self.l_name,"username":self.username,"email_id":self.email_id,"password":self.password,
             "emp_salary":self.emp_salary,"emp_pd_no":self.emp_pf_no,"join_date":self.join_date,"pan_id":self.pan_id,"leave_balance":self.leave_balance,}
        print(dic)
        #database().insert_row("Emp_Creation_table",dic)
    def list_emp_details(self):
        pass
    def emp_leave_request(self):
        pass
    def emp_account_del(self):
        pass
obj=adminconsole()
obj.create_emp_account()
