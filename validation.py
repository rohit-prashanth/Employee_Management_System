import datetime
import re

# ref='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,20}$'
ref='\w[a-z_.]\D*@ojas-it[.]com'

def emp_emailvalidation():
    email = input("enter ur email::-")
    while True:

        if re.search(ref,email):
            return email
            break
        else:
            print("invalid email")
            email = input("enter ur email::-")
            continue

val=emp_emailvalidation()
print(val)

def emp_usernamevalidation():

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
