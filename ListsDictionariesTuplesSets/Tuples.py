if __name__ == '__main__':

    # Similar to lists, however they have one key difference - immutability
    # Once an element is inside a tuple, it can not be reassigned

    t = (1, 2, 3)
    mylist = [1, 2, 3]

    print(t)
    print(mylist)
    print(type(t))
    print(type(mylist))
    print(len(t))
    print(len(mylist))

    t = ("a", "a", "b")
    print(t)
    print(t.count("a"))
    print(t.index("b"))

