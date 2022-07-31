a = {"orange", "banana", "mango", "daal"}
print(type(a))

# b = set("dhaka", "ornage", "anaheim", "sylhet")
# print(type(b))

c = set("skjnkfsjshiks")
print(type(c))

d = {"a", "s", "s", "r"}
print(type(d))

a = {"orange", "banana", "mango", "daal", "banana", "mango"}
print(a)

# a = {"orange", "banana", "mango", "daal"}
# print(a[0])

a.add("pineapple")
print(a)

a.update("pear", "berry", "strawberry")
print(a)

a.update({"pear", "berry", "strawberry"})
print(a)

a.remove("t")
print(a)

a.discard("s")
print(a)

a.discard("cherry")
print(a)

a.pop()
print(a)

a.clear()
print(a)

x = {1, 3, 4, 9}
y = {2, 3, 4, 5, 6, 8, 7, 9}
print(x.union(y))
print(x.intersection(y))
print(x.difference(y))
print(y.difference(x))