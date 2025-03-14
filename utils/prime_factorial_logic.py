def calculate_factorial(n):
    """Calculates the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError('Input must be a non-negative integer.')
    if n in [0, 1]:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(num):
    """Checks if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_factorial(n):
    """Returns the factorial of n if n is prime, else raises an error."""
    if is_prime(n):
        return calculate_factorial(n)
    else:
        raise ValueError('Input must be a prime number.')