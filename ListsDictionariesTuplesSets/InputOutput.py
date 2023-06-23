if __name__ == '__main__':

    myFile = open("myfile.txt")
    print(myFile.read())
    myFile.seek(0)
    print(myFile.read())
    myFile.seek(0)
    print(myFile.readline())
    myFile.close()

    myFile2 = open("D:\\Courses\\UdemyPythonCourse\\UdemyPythonCourse\\ListsDictionariesTuplesSets\\myfile.txt")
    print(myFile2.read())
    myFile2.close()

    print("next method test -----")
    with open("myfile.txt") as myNewFile:
        contents = myNewFile.read()
        print(contents)
        print(contents)

    with open("my_new_file.txt", mode='w') as f:
        f.write("ONE ON FIRST \nTWO ON SECOND \nTHREE ON THIRD")

    with open("my_new_file.txt", mode='r') as f:
        contents = f.read()
        print(contents)

    with open("my_new_file.txt", mode='a') as f:
        f.write("\nFOUR ON FOURTH")

    print()
    with open("my_new_file.txt", mode='r') as f:
        contents = f.read()
        print(contents)

    with open("asdf.txt", mode='w') as f:
        f.write("I CREATED THIS FILE!")

    with open("asdf.txt", mode='r') as f:
        contents = f.read()
        print(contents)
