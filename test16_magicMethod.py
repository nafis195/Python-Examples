# comparison magic methods

a = 5
b = 9

print(a.__eq__(b))
print(a.__ne__(b))
print(a.__lt__(b))
print(a.__gt__(b))
print(a.__le__(b))
print(a.__ge__(b))


# airthmatic magic methods

a = 5
b = 7

print(a.__add__(b))
print(a.__sub__(b))
print(a.__mul__(b))
print(b.__mod__(a))
print(b.__pow__(a))
print(b.__floordiv__(a))


# type convertion magic methods

a = 5
print(type(a))
a = a.__float__()
print(type(a))
a = a.__str__()
print(type(a))
a = a.__repr__()
print(type(a))


# more magic methods

a = "bangladesh"
b = "desh"

print(a.__len__())
print(a.__iter__())
print(list(a.__iter__()))
print(a.__contains__(b))