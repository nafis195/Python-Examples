a = ("onion", "potato", "ginger", "cucumber")
print(type(a))

b = ("dhaka", "sylhet", "satkhira", 1, "orange", 3.141592653589)
print(type(b))

print(b[0])
print(b[2])
print(b[1:4])
print(b[:5])
print(b[2:])
print(b[3:])

print(type(b[0]))
print(type(b[3]))
print(type(b[4]))
print(type(b[5]))

b + ('new',)
print(b)

print(len(b))

a = ("onion", "potato", "ginger", "cucumber", "potato")
print(a.count("potato"))