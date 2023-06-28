from random import shuffle


def shuffle_list(mylist):

    shuffle(mylist)
    return mylist


def player_guess():

    guess  = ' '
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number 0, 1, or 2: ")
    return int(guess)


def check_guess(mylist, guess):
    if mylist[guess] == '0':
        print("Correct!")
    else:
        print("Wrong guess!")
        print(mylist)


if __name__ == '__main__':

    # example = [1, 2, 3, 4, 5, 6, 7]
    # print(example)
    # shuffle_list(example)
    # print(example)

    game_list = [' ', '0', ' ']
    shuffled_list = shuffle_list(game_list)
    guess = player_guess()
    check_guess(shuffled_list, guess)

