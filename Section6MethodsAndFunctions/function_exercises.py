def hello():
    print("Hello World")


def my_name(name):
    print("Hello {}".format(name))


def hello_goodbye(a):
    if a:
        return "Hello"
    else:
        return "Goodbye"


def return_boolean(x, y, z):
    if z:
        return x
    else:
        return y


def sum_two(num1, num2):
    return num1 + num2


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def is_greater(num1, num2):
    if num1 > num2:
        return True
    else:
        return False


def sum_args(*args):
    return sum(args)


def list_args(*args):
    my_list = []
    for item in args:
        if item % 2 == 0:
            my_list.append(item)
    return my_list


def modded_string(mystring):
    mod_string = []
    index = 0
    for letter in mystring:
        if index % 2 == 0:
            mod_string.append(letter.upper())
        else:
            mod_string.append(letter.lower())
        index += 1
    return ''.join(mod_string)


if __name__ == '__main__':

    hello()
    my_name("Steven")
    print(list_args(2, 1, 4, 6, 7, 9))
    print(modded_string("hello world"))
