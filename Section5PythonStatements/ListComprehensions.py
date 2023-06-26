if __name__ == '__main__':

    myString = "hello"
    myList = []

    # simple method to put characters of myString into myList
    for letter in myString:
        myList.append(letter)

    # list comprehension method to put characters of myString into myList2
    myList2 = [letter for letter in myString]

    print(myList)
    print(myList2)

    myList3 = [num for num in range(0, 11)]
    myList4 = [num ** 2 for num in range(0, 11)]
    # using if with list comprehension
    myList5 = [num ** 2 for num in range(0, 11) if num % 2 == 0]

    print(myList3)
    print(myList4)
    print(myList5)

    # using if else with list comprehension changes the order of the statement
    # can get confusing
    results = [x if x % 2 == 0 else "Odd" for x in range(0, 11)]
    print(results)

    myList6 = []
    # nested loops
    for x in [2, 4, 6]:
        for y in [1, 10, 1000]:
            myList6.append(x * y)
    print(myList6)

    # nested loops in list comprehension
    myList7 = [x * y for x in [2, 4, 6] for y in [1, 10, 1000]]
    print(myList7)
    
