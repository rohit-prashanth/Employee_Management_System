import datetime
import re
from data_base import Database
#Database().FUNCTION NAME

# ref='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,20}$'
ref='\w[a-z_.]\D*@ojas-it[.]com'

# def emp_emailvalidation():
#     # email = input("enter ur email::-")
#    while True:
#        email = input("enter ur email::-")
#        if re.search(ref,email):
#             return email
#             break
#        else:
#             print("invalid email")
#             # email = input("enter ur email::-")
#             continue

# val=emp_emailvalidation()
# print(val)

# def emp_useridvalidation():
#     Database().read_table()
#     usinpt=input("enter userid")
#     while True:
#
#         if usinpt.isalphanum():
#              #compare user inpt with data base values
#             return usinpt
#             break
#         else:
#             print("invalid userid")
#          usinpt = input("enter ur userid::-")
#             continue
# usid=emp_useridvalidation()
# print(usid)

def emp_usernamevalidation():

   while True:
       inpt= input("enter ur username::-")
       if inpt.isalnum():
            return inpt
            break
       else:
            print("invalid username")
            # email = input("enter ur email::-")
            continue


user=emp_usernamevalidation()
print(user)









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
