def say_hello(name):
    print(f"Hello {name}")


def add_num(num1, num2):
    return num1 + num2


def return_result(a, b):
    return a + b


def even_check(number):
    return number % 2 == 0


def check_even_list(num_list):
    even_numbers = []

    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers


if __name__ == '__main__':

    say_hello("kevin")
    result = return_result(5, 9)
    print(result)
    print(check_even_list([1, 2, 3, 4, 5]))


