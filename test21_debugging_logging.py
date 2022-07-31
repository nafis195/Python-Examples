import logging

logging.basicConfig(filename="test21_test.log", level=logging.INFO)

a = 10
b = 0

try:
    temp = a/b
    print(temp)
except ZeroDivisionError as e:
    logging.exception(e)