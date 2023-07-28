def prob1():
    try:
        for i in ['a', 'b', 'c']:
            print(i**2)
    except:
        print("Type error!")


def prob2():
    try:
        x = 5
        y = 0
        z = x/y
    except:
        print("Error!!")
    finally:
        print("All done")


def prob3():
    is_valid = False
    while not is_valid:
        try:
            n = int(input("Enter a number: "))
        except:
            print("Please try again!  \n")
        else:
            print("Your number squared is: ")
            print(n**2)
            is_valid = True


if __name__ == '__main__':
    prob3()

