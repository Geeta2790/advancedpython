import unittest
from my_module import MyClass

class TestMyClass(unittest.TestCase):
    """
    Test suite for MyClass methods.
    """

    def setUp(self):
        """
        Initialize a MyClass instance for testing.
        """
        self.instance = MyClass()

    def test_method_one(self):
        """
        Test the behavior of method_one with valid input.
        """
        result = self.instance.method_one(5)
        self.assertEqual(result, 25)

    def test_method_one_invalid(self):
        """
        Test the behavior of method_one with invalid input.
        """
        with self.assertRaises(ValueError):
            self.instance.method_one(-1)

    def test_method_two(self):
        """
        Test the behavior of method_two with specific conditions.
        """
        self.instance.set_value(10)
        result = self.instance.method_two()
        self.assertTrue(result)

    def test_complex_logic(self):
        """
        Test method with complex conditions and multiple assertions.
        """
        self.instance.set_value(0)
        self.assertEqual(self.instance.method_two(), False)
        self.instance.set_value(15)
        self.assertEqual(self.instance.method_two(), True)
        self.assertEqual(self.instance.method_one(3), 9)

if __name__ == '__main__':
    unittest.main()