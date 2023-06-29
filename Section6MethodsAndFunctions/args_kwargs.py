def myfunc(a, b):
    # Returns 5% of the sum of a and b
    return sum((a, b)) * 0.05


# *args returns a tuple with as many arguments that passed into the function
def myfunc2(*args):
    return sum(args) * 0.05


def myfunc3(**kwargs):
    print(kwargs)
    if "fruit" in kwargs:
        print("My fruit of choice is {}".format(kwargs["fruit"]))
    else:
        print("I did not find any fruit here")


def myfunc4(*args, **kwargs):
    print("I would like {} {}".format(args[0], kwargs["food"]))


if __name__ == '__main__':
    print(myfunc2(40, 60, 200, 500))
    print(myfunc3(fruit="apple", veggie="lettuce"))
    print(myfunc4(10, 20, 30, fruit="orange", food="eggs", animal="dog"))

