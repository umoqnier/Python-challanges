"""
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hint: 
search isdigit & isalpha

"""

def main():
    word = input("Enter your string please: ")
    word = word.replace(" ", "")  # Quitando espacios blancos para que sea mas rapida la pasada
    letters, digits = 0, 0
    for letter in word:
        if letter.isdigit():
            digits += 1
        elif letter.isalpha():
            letters += 1
    print("LETTERS", letters)
    print("DIGITS", digits)

if __name__ == '__main__':
    main()