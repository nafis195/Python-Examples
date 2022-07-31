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


my_calculator = Calculator()

temp = my_calculator.addition(12, 23)
print(temp)

temp = my_calculator.subtraction(45, 27)
print(temp)

temp = my_calculator.multiplication(2, 18)
print(temp)

temp = my_calculator.division(43, 0)
print(temp)




class Calculator:
    # this class is for addition, subtraction, multiplication, division

    def __init__(self, a, b):
        # this is constructor class
        self.a = a
        self.b = b

    def addition(self):
        # this function is for addition
        return self.a+self.b

    def subtraction(self):
        # this function is for subtraction
        return self.a-self.b

    def multiplication(self):
        # this function is for multiplication
        return self.a*self.b

    def division(self):
        # this function is for division
        try:
            self.a/self.b
        except ZeroDivisionError:
            return "it's not possible to divide a number by zero."


new_calculator = Calculator(23, 35)

print(new_calculator.addition())
print(new_calculator.subtraction())
print(new_calculator.multiplication())
print(new_calculator.division())
