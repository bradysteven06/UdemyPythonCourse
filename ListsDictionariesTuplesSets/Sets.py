if __name__ == '__main__':

    # Sets are unordered collections of unique elements
    # Meaning there can only be one representative of the same object

    mySet = set()
    mySet.add(1)
    print(mySet)

    mySet.add(2)
    print(mySet)
    mySet.add(2)
    print(mySet)

    myList = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3]
    newSet = set(myList)
    print(newSet)
