import datetime
import re
from data_base import Database
import getpass
from string import punctuation
#Database().FUNCTION NAME

class Validation:

    def emp_emailvalidation(self):
        # ref='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,20}$'
        ref = '\w[a-z_.]\D*@ojas-it[.]com'
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
        db = Database().read_table('Emp_Creation_Table')
        # usinpt=input("enter userid")
        lst = []
        for i in db:
            lst.append(i[2])
        while True:
            usinpt = input("enter userid")
            for i in lst:
                if i == usinpt:
                    print("unique id")
                    continue
            else:
                return usinpt
                break
    def emp_usernamevalidation(self):
        while True:
            inpt = input("enter ur firstname::-")
            inpt1 = input("enter ur last name::-")
            if inpt.isalpha() and inpt1.isalpha():
                return inpt, inpt1
                break
            else:
                print("invalid username")
                continue

    def emp_passwordvalidation(self):
        while True:
            password = input("enter u r password::-")
            if ' ' in password:
                print( 'there is a space in password')
                continue

            if len(password) not in range(8,17):
                print('password should between in min 8 & max 16 characters')
                continue

            special_chars=[True for x in password if x in punctuation]
            if len(special_chars)==0:
                print( 'your password should have one special character')
                continue

            nums=any(x.isdigit() for x in password)
            if not  nums:
                print( "you should have atleast 1 digit in your password")
                continue

            else:
                return password
                break

    def emp_salaryvalidation(self):
        while True:
            try:
                salary = float(input("enter salary"))
                if salary:
                    return salary
            except:
                print("enter valid salary ")
                continue
    def emp_pfno_validation(self):
        while True:
            pfno=input("enter pf no")
            if pfno.isalpha():
                continue
            if pfno.isnumeric():
                continue
            if pfno.isalnum():
                return pfno
            else:
                continue
    def date_validation(self):
        while True:
            date_string = input("enter date in YYYY-MM-DD format")
            format = "%Y-%m-%d"
            try:
                if datetime.datetime.strptime(date_string, format):
                    return datetime.datetime.strptime(date_string, format)
                    break
            except:
                print("Incorrect data format, should be YYYY-MM-DD")
                continue
    def panid_validation(self):
        while True:
            pfno=input("enter pan no")
            if pfno.isalpha():
                continue
            if pfno.isnumeric():
                continue
            if pfno.isalnum():
                return pfno
            else:
                continue
class Loginconsole_validations:
    def username_validation(self):
        while True:
            username=input("enter username")
            password=input("enter password")
            us_data=Database().read_table("Emp_Creation_Table")
            dic={}
            for i in us_data:
                dic[i[2]]=i[4]
            if username in dic.keys():
                if password == dic[username]:
                    print("success full")
                else:
                    print("entered credentials are wrong")
                    continue
            else:
                print("entered credentials are wrong")
#obj = Loginconsole_validations()
#obj.username_validation()






# password length be min 8 char and max length is 16 in that upper&lower cases &special symbols and numbers
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
