if __name__ == '__main__':

    my_list = [1, 2, 3]
    print(my_list)
    my_list = ["STRING", 100, 23.2]
    print(my_list)
    print(len(my_list))

    my_list2 = ["one", "two", "three"]
    print(my_list2[0])
    print(my_list2[1:])

    my_list3 = ["four", "five"]
    print(my_list2 + my_list3)

    new_list = my_list2 + my_list3
    new_list[0] = "ONE ALL CAPS"
    print(new_list)
    new_list.append("six")
    print(new_list)
    new_list.append("seven")
    popped_item = new_list.pop()
    popped_item2 = new_list.pop(0)
    print(popped_item)
    print(popped_item2)

    new_list = ['a', 'e', 'x', 'b', 'c']
    num_list = [4, 1, 8, 3]

    print(new_list)
    print(num_list)
    new_list.sort()
    num_list.sort()
    print(new_list)
    print(num_list)
    num_list.reverse()
    print(num_list)
