import datetime
import re
from Data_base import Database
#Database().FUNCTION NAME

class Validation:

    def emp_emailvalidation(self):
        ref='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,20}$'
        #ref = '\w[a-z_.]\D*@ojas-it[.]com'
        while True:
            email = input("enter ur email::-")
            re.search(ref,email)
            if re.search(ref,email):
                return email
                break
            else:
                print("invalid email")
                continue


    def emp_useridvalidation(self):
        db=Database().read_table('Emp_Creation_Table')
        #usinpt=input("enter userid")
        lst=[]
        for i in db:
            lst.append(i[2])
        while True:
            usinpt = input("enter userid")
            for i in lst:
                if i==usinpt:
                    print("unique id")
                    continue
                else:
                    return usinpt
                    break




    def emp_usernamevalidation(self):
       while True:
           inpt= input("enter ur firstname::-")
           inpt1 = input("enter ur last name::-")
           if inpt.isalpha() and inpt1.isalpha():
                return inpt,inpt1
                break
           else:
                print("invalid username")
                continue
#obj=Validation()
#obj.emp_emailvalidation()





# password length be min 8 char and max length is 16 in that upper&lower cases &special symbols
#def changepassword():






# class validation:
#     def __init__(self):
#         pass
#     def emp_usernamevalidation(username):
#
#
#     def emp_salaryvalidation(self):
#
#     def emp_datevalidation(self):
#
#     def emp_leave_request_validation(emp_username, from_date, to_date):
#         print("it is a valid ")
