"""
Write a program that asks the user how many Fibonnaci numbers to generate and
then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.

Hint
The Fibonnaci seqence is a sequence of numbers where the next number
in the sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13,


"""
def fibonnacci():
    number = int(input("Introduce a number of Fibonnaci steps:"))
    lastNumber = 1
    thisNumber = 1
    nextNumber = 0
    listNumber = [lastNumber, thisNumber]

    for q in range(number):
        nextNumber = lastNumber + thisNumber
        listNumber.append(nextNumber)
        lastNumber = thisNumber
        thisNumber = nextNumber

    print(listNumber)

if __name__ == '__main__':
    fibonnacci()
