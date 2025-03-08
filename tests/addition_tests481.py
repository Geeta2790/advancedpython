def test_addition():
    """Test the addition function."""
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    assert addition(-1, -1) == -2

def addition(a, b):
    """Return the sum of a and b."""
    return a + b