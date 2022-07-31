a = ["onion", "potato", "ginger", "cucumber"]
print(type(a))

print(a[0])
print(a[1])
print(a[1:3])
print(a[:3])
print(a[2:])

a[0] = "rice"
a[3] = 570
print(a)

a.append("new")
print(a)

a.insert(2, "python")
print(a)

a.extend(["pen", "book", "pencil"])
print(a)

a + ["dhaka", "anaheim", "USA"]
print(a)

del a[5]
print(a)

a.remove("python")
print(a)

del a[-2]
print(a)

a.pop()
print(a)

print(len(a))

a.append("rice")
print(a)
print(a.count("rice"))

a.reverse()
print(a)

b = [23, 3, 5, 100, 1, 8]
b.sort()
print(b)