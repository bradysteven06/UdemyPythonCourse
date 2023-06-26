if __name__ == '__main__':

    x = 0

    while x <= 5:
        print(f"The current value of x is {x}")
        x += 1

    # break: Breaks out of the current closest enclosing loop.
    # continue: Goes to the top of the closest enclosing loop.
    # pass: Does nothing at all.

    x = [1, 2, 3]

    for item in x:
        # won't run with just a comment
        pass # use this as filler to pass through the loop and do nothing
    print("End of my script")

    myString = "Sammy"

    for letter in myString:
        if letter == 'a':
            continue
        print(letter)

    x = 0

    while x < 5:
        if x == 2:
            break
        print(x)
        x += 1
