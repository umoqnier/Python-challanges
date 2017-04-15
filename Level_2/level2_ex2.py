"""
Given an array of equal-length strings, check if it is possible to rearrange
the strings in such a way that after the rearrangement the strings at consecutive
positions would differ by exactly one character.

Hint
For inputArray = ["aba", "bbb", "bab"], the output should be
stringsRearrangement(inputArray) = false;
For inputArray = ["ab", "bb", "aa"], the output should be
stringsRearrangement(inputArray) = true.

Hace falta depurar :( :(
"""

def stringsRearrangement(inputArray):
    def closeWords(word1, word2):
        return sum(letter[0] != letter[1] for letter in zip(word1, word2)) == 1

    listArray = inputArray.split(",")
    firstLen = len(listArray[0])
    for x in listArray:
        if len(x) != firstLen:
            print("All items must have the same lenght!")
            return False

    firstItem = listArray[0]
    newArray = [x for x in listArray if x != firstItem]
    index = 3
    for q in range(index):
        if closeWords(firstItem, newArray[0]):
            firstItem = newArray[0]
            newArray.remove(firstItem)
    if len(newArray) == 0:
        return True
    else:
        return False


print(stringsRearrangement("ab,bb,aa"))
