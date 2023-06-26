if __name__ == '__main__':

    st = "Print only the words that start with s in this sentence"

    wordList = st.split()
    for word in wordList:
        if "s" in word and word[0] == "s":
            print(word)

    for num in range(0, 11, 2):
        print(num)

    myList = [num for num in range(1, 51) if num % 3 == 0]
    print(myList)

    st2 = "Print every word in this sentence that has an even number of letters"
    wordList2 = st2.split()
    for word in wordList2:
        if len(word) % 2 == 0:
            print(word)

    for num in range(1, 101):
        if num % 3 == 0:
            if num % 5 == 0:
                print("FizzBuzz")
            else:
                print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

    st3 = "Create a list of the first letters of every word in this string"
    wordList3 = st3.split()
    letterList = [word[0] for word in wordList3]
    print(letterList)
