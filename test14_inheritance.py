class Calculator:
    # class for addition, subtraction, multiplication, division

    def addition(self, a, b):
        # function for addition
        return a+b

    def subtraction(self, a, b):
        # function for subtraction
        return a-b

    def multiplication(self, a, b):
        # function for multiplication
        return a*b

    def division(self, a, b):
        #function for division
        try:
            return a/b
        except ZeroDivisionError:
            return "it's impossible to divide by zero"


class ChildCalculator(Calculator):
    # this is a child class of Calculator class

    def square(self, a):
        # this function is for square
        return a*a

    def cube(self, a):
        # this function is for cube
        return a*a*a


my_calculator = ChildCalculator()

temp = my_calculator.addition(12, 23)
print(temp)

temp = my_calculator.subtraction(45, 27)
print(temp)

temp = my_calculator.multiplication(2, 18)
print(temp)

temp = my_calculator.division(43, 0)
print(temp)

temp = my_calculator.square(4)
print(temp)

temp = my_calculator.cube(3)
print(temp)



# Method Overriding Example

class Calculator:
    # class for addition, subtraction, multiplication, division

    def addition(self, a, b):
        # function for addition
        return a+b

    def subtraction(self, a, b):
        # function for subtraction
        return a-b

    def multiplication(self, a, b):
        # function for multiplication
        return a*b

    def division(self, a, b):
        #function for division
        try:
            return a/b
        except ZeroDivisionError:
            return "it's impossible to divide by zero"


class ChildCalculator(Calculator):
    # this is a child class of Calculator class

    def addition(self, a, b, c):
        # this is an example of method overriding
        return a+b+c

    def square(self, a):
        # this function is for square
        return a*a

    def cube(self, a):
        # this function is for cube
        return a*a*a


my_calculator = ChildCalculator()

# print(my_calculator.addition(12, 23))
print(my_calculator.square(4))
print(my_calculator.cube(3))
print(my_calculator.addition(12, 23, 34))