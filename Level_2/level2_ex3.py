"""
Write a password generator in Python. Be creative with how you generate 
passwords - strong passwords have a mix of lowercase letters, uppercase letters, 
numbers, and symbols. The passwords should be random, generating a new password 
every time the user asks for a new password. 
Include your run-time code in a main method.


Extra:

Ask the user how strong they want their password to be. For weak passwords, 
pick a word or two from a list.


"""

import random
import string


def take_some_item(field):
    return field[random.randint(0, len(field)-1)]


def main():
    new_pass = list()
    weak = ['password', '123456', '1q2w3e4r', '1234qwer', 'qwerty', 'iloveyou', '111111', 'abc123']
    strong = list(string.ascii_letters) + list(string.digits)
    strongest = list(string.ascii_letters) + list(string.digits) + list(string.punctuation)
    print("How strong you want your password? [1|2|3]")
    print("1: So much strong :D")
    print("2: Strong :|")
    print("3: Not really strong :(")
    flag = input(">> ")
    if flag == "1":
        for i in range(15):
            new_pass.append(take_some_item(strongest))
        print("Your password is: " + "\'" + ''.join(new_pass) + "\'", end='')
    elif flag == "2":
        for i in range(10):
            new_pass.append(take_some_item(strong))
        print("Your password is: " + "\'" + ''.join(new_pass) + "\'", end='')
    elif flag == "3":
        print("Your password is: " + "\'" + take_some_item(weak) + "\'", end='')
    else:
        print("WTF dude? This option is invalid. u.u")


if __name__ == '__main__':
    main()