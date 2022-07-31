import sys


# sys.argv
print(sys.argv)
print(type(sys.argv))

for arg in sys.argv:
    print(arg)



# sys.exc_info()
try:
    print(10/0)
except ZeroDivisionError:
    print(sys.exc_info())



# sys.executable (only for prinitng python's interpreter's executable path)
print(sys.executable)



# sys.exit()
# sys.exit()
# sys.exit(1)
# sys.exit("error message")



# sys.path()
print(type(sys.path))
print(len(sys.path))

for path in sys.path:
    print(path)

sys.path.append('/home/ugcoder')
print(sys.path)



# sys.platform
print(sys.platform)



