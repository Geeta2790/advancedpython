def test_sum_function():
    """
    Test the sum function to ensure it adds numbers correctly.
    """
    result = sum_function(2, 3)
    assert result == 5
    result = sum_function(-1, 1)
    assert result == 0
    result = sum_function(0, 0)
    assert result == 0
    result = sum_function(-5, -5)
    assert result == -10
    result = sum_function(1.5, 2.5)
    assert result == 4.0