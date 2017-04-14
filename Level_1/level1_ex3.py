"""
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.

Hint
Use __init__ method to construct some parameters


"""

class StrCool():

    def __init__(self):
        self.__strg = None

    def getString(self):
        self.__strg = input("Introduce a string: ")
        print("Your string is %s" % self.__strg)
