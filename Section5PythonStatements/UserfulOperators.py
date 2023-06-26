from random import shuffle
from random import randint

if __name__ == '__main__':

    # generates numbers 0 to 9 using range(start, stop, step)
    for num in range(10):
        print(num)

    myList = list(range(0, 50, 2))
    print(myList)

    # generates tuples of the index and letter in the word variable
    word = "abcde"
    for index, letter in enumerate(word):
        print(index)
        print(letter)
        print("\n")

    myList1 = [1, 2, 3, 4]
    myList2 = ['a', 'b', 'c']
    myList3 = [100, 200, 300]

    # creates tuple sets from the given lists
    # stops at the end of the shortest list
    for item in zip(myList1, myList2, myList3):
        print(item)

    # the 'in' operator checks if item is in container
    print(1 in myList1)
    print(5 in myList1)

    print(myList)
    shuffle(myList)
    print(myList)

    randomNum = randint(0, 100)
    print(randomNum)

    result = input("What is your favorite number? ")
    print(type(result))
    result = int(result)
    print(type(result))