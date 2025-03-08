def test_addition():
    """Test case for addition function."""
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0

def addition(a, b):
    """Returns the sum of two numbers."""
    return a + b