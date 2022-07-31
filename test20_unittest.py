import unittest
from test20_unitTesting import add, is_even

class MyTest(unittest.TestCase):

    def test_add(self):
        # function to test the add function
        self.assertEqual(add(2, 3), 5)

    def test_is_even(self):
        # function to test is_even function
        self.assertTrue(is_even(2))


if __name__ == "__main__":
    unittest.main()