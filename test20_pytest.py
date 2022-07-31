from test20_unitTesting import add, is_even

def test_add():
    # function to test add
    assert add(2, 3) == 5

def test_is_even():
    # function to test is_even
    assert is_even(4) == True