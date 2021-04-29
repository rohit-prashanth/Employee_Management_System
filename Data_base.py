import pymysql

conn = pymysql.connect(user='root',password='',host="localhost",database="Employee_leave_management_system")
# print(conn)
cur = conn.cursor()
# cur.execute("show databases")
# for j in cur:
#     print(j)
class Database:

    def create_table(self):    
        pass
    def read_table(self):
        pass

    def update_table(self):
        pass

    def delete_row(self):
        pass
        
    