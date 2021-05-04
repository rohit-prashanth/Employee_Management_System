from Data_base import Database
from validation import validation
class Adminconsole:
    def create_emp_account(self):
        self.f_name=input("enter first name")
        self.l_name=input("enter last name")
        self.username=input("create user name")
        self.email_id=Validation().emp_usernamevalidation()
        self.password=input("enter password")
        self.emp_salary=float(input("enter employee salary"))
        self.emp_pf_no=input("enter pf no")
        self.join_date=input("enter joining date")
        self.pan_id=input("ener pancard number")
        self.leave_balance=int(input("enter leave balance days"))
        dic={"first_name":self.f_name,"last_name":self.l_name,"username":self.username,"email_id":self.email_id,"password":self.password,
             "emp_salary":self.emp_salary,"emp_pf_no":self.emp_pf_no,
             "join_Date":self.join_date,"pan_no":self.pan_id,"leave_balance":self.leave_balance,}
        Database().insert_row("Emp_Creation_Table",dic)
    def list_emp_details(self):
        username=input("enter username to know the employee details")
        if username:
            Database().read_table("emp_creation_table",username)
        else:
            Database().read_table("emp_creation_table")
    def emp_leave_request(self):
        Database().read_table("Leave_Request_Table")
        self.username=input("enter username")
        self.status=input("enter status")
        Database().update_table("Leave_Request_Table",self.username,'status',self.status)
    def emp_account_del(self):
        del_row=input("enter username to delete")
        Database().delete_row("emp_creation_table",del_row)
#obj=adminconsole()
#obj.create_emp_account()
#obj.emp_account_del()
#obj.list_emp_details()
#obj.emp_leave_request()
