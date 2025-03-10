import unittest

class TestMathOperations(unittest.TestCase):
    """
    Test suite for verifying mathematical operations.
    """

    def setUp(self):
        """
        Initialize variables for testing.
        """
        self.num1 = 10
        self.num2 = 5

    def test_addition(self):
        """
        Test the addition of two numbers.
        """
        self.assertEqual(self.num1 + self.num2, 15)

    def test_subtraction(self):
        """
        Test the subtraction of two numbers.
        """
        self.assertEqual(self.num1 - self.num2, 5)

    def test_multiplication(self):
        """
        Test the multiplication of two numbers.
        """
        self.assertEqual(self.num1 * self.num2, 50)

    def test_division(self):
        """
        Test the division of two numbers.
        """
        self.assertEqual(self.num1 / self.num2, 2)

if __name__ == '__main__':
    unittest.main()