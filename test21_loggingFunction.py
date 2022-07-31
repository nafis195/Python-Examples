import logging
from test21_testingFunction import add, is_even

# general format in the log file
# logging.basicConfig(filename="test21_test.log", level=logging.INFO)

# adding format in the log file
logging.basicConfig(filename="test21_test.log", format= "%(asctime)s - %(name)s - %(message)s", level=logging.INFO)

logging.info("we are calling our add function")
temp = add(12, 78)
print(temp)
logging.info("add function executed, task completed")

logging.info("we are calling out is_even function")
temp = is_even(2)
print(temp)
logging.info("add function executed, task completed")