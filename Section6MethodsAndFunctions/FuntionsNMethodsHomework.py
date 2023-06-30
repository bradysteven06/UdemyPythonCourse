import math
import string


def vol(rad):
    return (4/3) * math.pi * (rad**3)


def range_check(num, low, high):
    return low <= num <= high


def up_low(my_string):
    up = 0
    low = 0
    for letter in my_string:
        if letter.isupper():
            up += 1
        elif letter.islower():
            low += 1
    return up, low


def unique_list(lst):
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x


def multiply(numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


def palindrome_check(s):
    s = s.replace(' ', '')
    return s == s[::-1]


def ispangram(str1, alphabet=string.ascii_lowercase):
    # Create a set of the alphabet
    alphaset = set(alphabet)

    # Remove spaces from str1
    str1 = str1.replace(" ", '')

    # Lowercase all strings in the passed in string
    # Recall we assume no punctuation
    str1 = str1.lower()

    # Grab all unique letters in the string as a set
    str1 = set(str1)

    # Now check that the alphabet set is same as string set
    return str1 == alphaset


if __name__ == '__main__':

    print(vol(2))
    print(range_check(5, 2, 7))
    print(up_low("Hellow Mr. Rogers, how are you this fine Tuesday?"))
    print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))
    print(multiply([1,2,3,-4]))
    print(palindrome_check('nurses run'))
    print(ispangram("The quick brown fox jumps over the lazy dog"))


