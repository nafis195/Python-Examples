a = {"name": "tommy ilmas", "email": "tommy@ilmas.com", "phone": "123456789", "country": "USA"}
print(a)
print(type(a))

b = dict()
print(type(b))

print(a["name"])
print(a["phone"])

a["name"] = "lester holt"
print(a)

b = {"city": "anaheim", "school": "CSUF", "job": "AWS"}
a.update(b)
print(a)

del a["phone"]
print(a)

a.clear()
print(a)

del a
# print(a)

a = {'name': 'lester holt', 'email': 'tommy@ilmas.com', 'country': 'USA', 'city': 'anaheim', 'school': 'CSUF', 'job': 'AWS'}
c = a.copy()
print(c)

print(a.get("name"))
print(a.get("home", "default is none"))

print("name" in a)
print("home" in a)

print(a.items())
print(a.keys())
print(a.values())