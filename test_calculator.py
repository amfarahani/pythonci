from calculator import product

def test_product_positive_numbers():
    assert product(2, 3) == 6

def test_product_with_zero():
    assert product(10, 0) == 0

def test_product_negative_numbers():
    assert product(-2, 4) == -8
