# while loop
n = 1
temp = 0
while n<=100:
    temp = temp + n
    n = n + 1
print(temp)


# for loop in list
a = ["orange", "anaheim", "irvine", "fullerton"]
for items in a:
    print(items)


# for loop in dictionary
a = {'name': 'lester holt', 'email': 'tommy@ilmas.com', 'country': 'USA', 'city': 'anaheim', 'school': 'CSUF', 'job': 'AWS'}
for stuffs in a:
    print(stuffs)


# for loop in string
a = "python"
for letters in a:
    print(letters)


# for loop using range
sum = 0
for numbers in range(1, 100):
    sum = sum + numbers
print(sum)


