from Data_base import Database
#from validation import validation
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
        dic={"first_name":self.f_name,"last_name":self.l_name,"username":self.username,"email_id":self.email_id,"password":self.password,
             "emp_salary":self.emp_salary,"emp_pf_no":self.emp_pf_no,"join_Date":self.join_date,"pan_no":self.pan_id,"leave_balance":self.leave_balance,}
        Database().insert_row("Emp_Creation_Table",dic)
    def list_emp_details(self):
        Database().read_table("emp_creation_table")
    def emp_leave_request(self):
        import pymysql
        conn = pymysql.connect(user='root',password='root',host="localhost")
        cur = conn.cursor()
        cur.execute("use Employee_leave_management_system")
        print("leave request for employee")
        self.username=input("enter username")
        self.from_date=input("enter from date")
        self.to_date=input("enter to date")
        self.no_of_days=int(input("enter number of days"))
        self.q=f"select leave_balance from emp_creation_table where username='{self.username}'"
        self.leave_balance=cur.execute(self.q)
        dic={"username":self.username,"from_date":self.from_date,"to_date":self.to_date,"no_of_days":self.no_of_days,"leave_balance":self.leave_balance,"status":"pending"}
        print(dic)
        Database().insert_row("Leave_Request_Table",dic)
    def emp_account_del(self):
        del_row=input("enter username to delete")
        Database().delete_row("emp_creation_table",del_row)
#obj=adminconsole()
#obj.create_emp_account()
#obj.emp_account_del()
#obj.list_emp_details()
#obj.emp_leave_request()
