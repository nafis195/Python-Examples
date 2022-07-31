# Reading a file
my_file = open('test11_file.txt', 'r')
content = my_file.read()
print(content)
my_file.close()


# Writing to a file
new_file = open("test11_file.txt", "w")
new_file.write("I born in Bangladesh")
new_file.close()


