"""
A website requires the users to input username and password to register. 
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1

Hint:
you need to use regular expressions
https://www.tutorialspoint.com/python/python_reg_expressions.htm 

"""
import re

passwords = input("Enter the paswords>> ")
pass_list = passwords.split(",")

for password in pass_list:
	obj_match = re.match("((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%]).{6,20})", password)
	if obj_match.group() == password:
		print(password)
		break
	else:
		print("Your passwords are so bad, try again D:")