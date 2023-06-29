def lesser_of_two_evens(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        if num1 < num2:
            return num1
        else:
            return num2
    else:
        if num1 > num2:
            return num1
        else:
            return num2


def animal_crackers(my_string):
    split_string = my_string.split()
    if split_string[0][0].lower() == split_string[1][0].lower():
        return True
    else:
        return False


def makes_twenty(num1, num2):
    if num1 + num2 == 20 or num1 == 20 or num2 == 20:
        return True
    else:
        return False


def old_macdonald(name):
    first_part = name[:3]
    second_part = name[3:]
    first_part = first_part.capitalize()
    second_part = second_part.capitalize()
    print(first_part)
    print(second_part)
    mystring = ""
    mystring = mystring.join(first_part)
    mystring = mystring.join(second_part)
    print(mystring)
    return mystring

if __name__ == '__main__':

    print(old_macdonald("macdonald"))


