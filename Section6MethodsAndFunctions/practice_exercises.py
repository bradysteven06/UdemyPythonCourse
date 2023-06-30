def lesser_of_two_evens(num1, num2):
    result = 0
    if num1 % 2 == 0 and num2 % 2 == 0:
        if num1 < num2:
            result = num1
        else:
            result = num2
    else:
        if num1 > num2:
            result = num1
        else:
            result = num2
    return result


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
    mylist = []
    mylist.append(first_part)
    mylist.append(second_part)
    return "".join(mylist)


def master_yoda(sentence):
    reverse_list = []
    for word in reversed(sentence.split()):
        reverse_list.append(word)
    return " ".join(reverse_list)


def almost_there(n):
    if abs(n - 100) <= 10 or abs(n - 200) <= 10:
        return True
    else:
        return False


def has_33(list_ints):
    first_three = False
    second_three = False
    for num in list_ints:
        if num == 3 and not first_three:
            first_three = True
        elif num != 3 and first_three:
            first_three = False
        elif num == 3 and first_three:
            second_three = True

    if first_three and second_three:
        return True
    else:
        return False


def paper_doll(my_string):
    characters = []
    for char in my_string:
        characters.append(char*3)
    return "".join(characters)


def blackjack(num1, num2, num3):
    sum_numbers = num1 + num2 + num3
    if sum_numbers <= 21:
        return sum_numbers
    elif sum_numbers > 21 and num1 == 11 or num2 == 11 or num3 == 11:
        sum_numbers -= 10
        if sum_numbers <= 21:
            return sum_numbers
        else:
            return "BUST"
    else:
        return "BUST"


def summer_69(num_list):
    sum_total = 0
    six_rule_active = False
    for num in num_list:
        if num == 6:
            six_rule_active = True
        elif num == 9:
            six_rule_active = False
        elif six_rule_active:
            pass
        else:
            sum_total += num
    return sum_total


def spy_game(num_list):
    first_zero = False
    second_zero = False
    for num in num_list:
        if num == 0:
            if not first_zero:
                first_zero = True
            elif first_zero:
                second_zero = True
        elif num == 7:
            if first_zero and second_zero:
                return True
            else:
                first_zero = False
        else:
            first_zero = False
            second_zero = False
    return False


def count_primes(num):
    prime_count = 0
    for number in range(2, num+1):
        is_prime = True
        for n in range(2, number):
            if number % n == 0:
                is_prime = False
        if is_prime:
            prime_count += 1
    return prime_count


def print_big(letter):
    big_letters = {'a': "  *  \n * * \n*****\n*   *\n*   *",
                   'b': "**** \n*   *\n****  \n*   *\n**** "}
    return big_letters[letter.lower()]


if __name__ == '__main__':

    print(old_macdonald("macdonald"))
    print(print_big('B'))
