# function with required argument
def add(a, b, c):
    return a+b+c

sum = add(1, 2, 3)
print(sum)


# function with keyword argument
def add(a, b, c):
    return a+b+c

sum = add(b=1, c=2, a=3)
print(sum)


# function with default argument
def add(a, b, c=5):
    return a+b+c

sum = add(1, 2)
print(sum)


# function with non-keyworded variable length argument
def add(*args):   # "*args" represents the non-keyworded variable length argument
    print(type(args))   # it creates a tuple and holds the values in the tuple

    temp = 0
    for number in args:
        temp = temp + number
    
    return temp

sum = add(1, 2, 22, 12, 17, 21, 98)
print(sum)


# function with keyworded variable length argument
def add(**kwargs):   # "**kwargs" represents the keyworded variable length argument
    print(type(kwargs))   # it creates a disctionary and holds the values in the dictionary

    temp = 0
    for number in kwargs:
        temp = temp + kwargs[number]
    
    return temp

sum = add(a=1, b=2, c=22, d=12, e=17, f=21, g=98)   # as it's keyworded variable length argument, we need to pass the keyworded argument/parameter when calling the function
print(sum)


# Recursion
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

print("Please input a number: ")
num = int(input())
print(factorial(num))


# Map Function
my_list = [2, 3, 4, 6, 7]
def square(x):
    return x*x

new_list = map(square, my_list)
print(new_list)
print(list(new_list))


# Filter Function
my_list = [2, 3, 4, 6, 8, 9]
def is_even(x):
    if(x%2 == 0):
        return True
    else:
        return False

new_list = filter(is_even, my_list)
print(new_list)
print(list(new_list))