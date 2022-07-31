def print_int(number):
    def get_in_as_str(number):
        print(str(number))
        return

    return get_in_as_str(number)

print_int(130)



# Built in Decorator

# @classmethod
class MyClass:
    # class named MyClass

    def __init__(self):
        # contructor class
        pass

    def square(self, x):
        # square function
        return x*x

    @classmethod
    def cube(self, x):
        # cube function
        return x*x*x


if __name__ == "__main__":
    myclass = MyClass()
    print(myclass.square(3))
    print(myclass.cube(3))
    print(MyClass.cube(3))   # we can call without creating the object as we used @classmethod, no error
    #print(MyClass.square(3))   # throws error as we didn't use @classmethod



# staticmethod
class MyClass:
    # class named MyClass

    def __init__(self):
        # contructor class
        pass

    def square(self, x):
        # square function
        return x*x

    @staticmethod   
    def cube(x):   # differece between staticmethod and classmethod is, staticmethod doesn't need the "self"
        # cube function
        return x*x*x


if __name__ == "__main__":
    myclass = MyClass()
    print(myclass.square(3))
    print(myclass.cube(3))
    print(MyClass.cube(3))   # we can call without creating the object as we used @classmethod, no error
    #print(MyClass.square(3))   # throws error as we didn't use @classmethod



# @property method
class MyClass:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name


if __name__ == "__main__":
    myclass = MyClass("Nafis", "Chowdhury")
    print(myclass.full_name)
    myclass.full_name = "New_Name"   # as we used @property method, so the full_name function is read only now and we can't add new attribute

