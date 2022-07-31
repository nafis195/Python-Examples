a = "bangla"
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
# print(a[6])

print(a[1:4])
print(a[:1])
print(a[:2])
print(a[:3])
print(a[2:])
print(a[4:])
print(a[-1])
print(a[-2])


number = 436.15645353400221309
print('%.2f' % number)
print('%.4f' % number)
print('%.5f' % number)


a = "bangla"
b = "desh"
print(a+b)


x = "dhaka"
y = "sylhet"
z = "barisal"
print(x + "-" + y + "-" + z)
print("-".join((x, y, z)))


print(a.capitalize())
print(a.upper())
print("BANGLADESH".lower())
print("BaNgLaDesh".swapcase())
print(len(a))
print(a.count("a"))


sentence = "how can a calm cram in a clean cream can"
print(sentence.count("c"))
print(sentence.count("c", 5))
print(sentence.count("c", 5, 9))
print(sentence.find("c"))
print(sentence.find("c", 5))
print(sentence.find("x"))
print(sentence.replace("c", "d"))
print(sentence.strip("?"))
print(sentence.replace("?", ""))
print(sentence.split(" "))