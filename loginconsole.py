import Database from data_base
import validation
import pymysql
from datetime import datetime
from 
conn = pymysql.connect(user='root',password='root',host="localhost")
cur = conn.cursor()
cur.execute("use Employee_leave_management_system")

class LoginConsole:
    def emp_search(emp_username):
        Data=Database().read_table('Emp_Creation_Table',username = emp_username)
        Data_dic={'first_name':Data[0],'last_name':Data[1],Data[2],Data[7]}
        
    def change_password(emp_username):
        pwd= input("enter the password")
        p=checkvalidate('Emp_Creation_Table',emp_username,'password',pwd)
        
        New_pwd=input("enter new pwd")
        confirm_pwd=input("enter new pwd")
        pd=emp_passwordvalidation(New_pwd)
        update_table('Emp_Creation_Table',emp_username,'password',pd)
        
    def request_leave(self):

        print("leave request for employee")
        self.username=input("enter username")
        self.from_date=input("enter from date")
        self.to_date=input("enter to date")
        a=date_validation(from_date,to_date)
        date_time_obj1 = datetime.strptime(a[0], '%d/%m/%y')
        date_time_obj2 = datetime.strptime(a[1], '%d/%m/%y')
        self.no_of_days=(date_time_obj2)-(date_time_obj1)
        self.leave_balance=cur.execute(self.q)
        dic={"username":self.username,"from_date":self.from_date,"to_date":self.to_date,"no_of_days":self.no_of_days,"leave_balance":self.leave_balance,"status":"pending"}
        print(dic)
        Database().insert_row("Leave_Request_Table",dic)
