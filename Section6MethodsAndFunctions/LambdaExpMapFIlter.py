def square(num):
    return num**2


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return "EVEN"
    else:
        return mystring[0]


def check_even(num):
    return num % 2 == 0


if __name__ == '__main__':

    my_nums = [1, 2, 3, 4, 5, 6]

    for item in map(square, my_nums):
        print(item)

    names = ["Stuart", "Kevin", "Bob", "Gru"]
    print(list(map(splicer, names)))

    print(list(filter(check_even, my_nums)))
    for n in filter(check_even, my_nums):
        print(n)

    print(list(map(lambda num: num**2, my_nums)))
    print(list(filter(lambda num: num % 2 == 0, my_nums)))

    print(list(map(lambda name: name[0], names)))

