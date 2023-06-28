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


def employee_check(work_hours):
    current_max = 0
    employee_of_month = ""

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    return (employee_of_month, current_max)


if __name__ == '__main__':

    say_hello("kevin")
    result = return_result(5, 9)
    print(result)
    print(check_even_list([1, 2, 3, 4, 5]))

    work_hours = [("Abby", 100), ("Billy", 850), ("Cassie", 800)]
    print(employee_check(work_hours))
    name, hours = employee_check(work_hours)
    print(name)
    print(hours)
