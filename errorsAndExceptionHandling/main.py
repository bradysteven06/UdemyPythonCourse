def ask_for_int():
    is_valid = False
    while not is_valid:
        try:
            result = int(input("Please provide a number: "))
        except:
            print("Whoops! That is not a number")
        else:
            is_valid = True
            print("Thank you")
        finally:
            print("End of try/except/finally")


if __name__ == '__main__':
    try:
        f = open('testfile', 'w')
        f.write("Write a test line")
    except TypeError:
        print("there was a type error!")
    except:
        print("All other exceptions")
    finally:
        print("I always run")

    ask_for_int()


