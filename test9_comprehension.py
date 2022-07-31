# list comprehension
my_list = [i**2 for i in range(20) if i%2==0]
print(my_list)


# set comprehension
my_set = ["nafis", "bangladesh", "CSE", "a", "b", "c"]
my_set = {i for i in my_set if len(i) > 1}
print(my_set)


# dictionary comprehension
a_list = ["name", "country", "job"]
b_list = ["nafis", "USA", "AWS"]
my_dict = {i:j for i,j in zip(a_list, b_list)}
print(my_dict)


x = [i for i in range(1, 11)]
y = [i for i in range(11, 20)]
z = zip(x, y)
z = list(z)
print(z)


new_dict = {"name": "dipto", "country": "bangladesh", "job": "cisco"}
reversed_dict = {key:value for value, key in new_dict.items()}
print(reversed_dict)