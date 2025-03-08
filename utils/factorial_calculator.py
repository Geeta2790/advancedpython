def calculate_factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    Returns the factorial of n.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial