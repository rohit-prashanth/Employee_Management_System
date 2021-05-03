import pymysql
conn = pymysql.connect(user='root',password='root',host='localhost')
cur=conn.cursor()
database=cur.execute("create database if not exists Employee_leave_management_system")
da=cur.execute("use Employee_leave_management_system")
class Database:                                                                             
    def create_table(self):    
        cur.execute('create table if not exists Emp_Creation_Table(first_name varchar(20),last_name varchar(20),username varchar(20),email_id varchar(50),password varchar(20),emp_salary varchar(15),emp_pf_no varchar(20),join_Date varchar(20),pan_no varchar(10),leave_balance varchar(10))')
#     #     pass
    def insert_row(self,table_name,column):
        query = f"insert into {table_name} values({column['first_name']},{column['last_name']},{column['username']},{column['email_id']},{column['password']},{column['emp_salary']},{column['emp_pf_no']},{column['join_Date']},{column['pan_no']},{column['leave_balance']})"

        cur.execute(query)
        conn.commit()
    # #     print(cur)
    # # def read_table(self):

    #     pass

    # def update_table(self):
    #     pass

    # def delete_row(self):
    #     pass

"""column = {'first_name':'sample','last_name':'123','username':'sample123','email_id':'sample','password':'123456','emp_salary':10000,'emp_pf_no':12355,'join_Date':'03-02-2021','pan_no':'ADGJ4568','leave_balance':2}  
obj = Database()
obj.create_table()  
obj.insert_row('Emp_Creation_Table',column) """

# query = f"insert into Emp(first_name,last_name,username,email_id,password,emp_salary,emp_pf_no,join_Date,pan_no,leave_balance)values({column['first_name']},{column['last_name']},{column['username']},{column['email_id']},{column['password']},{column['emp_salary']},{column['emp_pf_no']},{column['join_Date']},{column['pan_no']},{column['leave_balance']})"
# print(query)
