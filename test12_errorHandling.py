try:
    with open("test.txt", "r") as myFile:
        content = myFile.read()
        print(content)
except:
    print("file doesn't exist")


try:
    with open("test.txt", "r") as myFile:
        content = myFile
        print(content)
except FileNotFoundError:
    print("File doesn't found")


try:
    myList = []
    print(myList[0])
except IndexError as e:
    print(e)


try:
    my_file = open("test.txt")
    content = my_file.read()
    i = int(content.strip())
except IOError as e:
    errno, strerror = e.args
    print("I/O error({0}): {1}".format(errno, strerror))
except ValueError:
    print("no valid integer in line")
except:
    print("Unexpected error!")


try:
    my_file = open("test.txt")
    content = my_file.read()
    i = int(content.strip())
except(IOError, ValueError):
    pass


try:
    a = 3
    b = 5
    c = a+b
except ValueError as e:
    print(e)
else:   # if there is no exception, then the code inside the else block will be executed
    print(c)


try:
    with open("test.txt", "r") as myFile:
        content = my_file.read()
        print(content)
except FileNotFoundError:
    print("file doesn't found")
finally:   # finally block will always execute at the end
    print("this finally block will always be executed")


try:
    raise NameError("it is a custom error message")   # built in exception
except NameError as e:
    print(e)

