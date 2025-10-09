import unittest
import sys

# We need to add the script's directory to the path to import it.
sys.path.append(r'c:\Users\rajneesh.x.sharma\OneDrive - Accenture\GitHub\WebSite1\WebSite1')

from test import factorial

class TestFactorial(unittest.TestCase):

    def test_zero(self):
        """Test the factorial of 0, which should be 1."""
        self.assertEqual(factorial(0), 1, "The factorial of 0 should be 1")

    def test_one(self):
        """Test the factorial of 1, which should be 1."""
        self.assertEqual(factorial(1), 1, "The factorial of 1 should be 1")

    def test_positive_number(self):
        """Test the factorial of a positive integer."""
        self.assertEqual(factorial(5), 120, "The factorial of 5 should be 120")
        self.assertEqual(factorial(6), 720, "The factorial of 6 should be 720")

    def test_negative_input(self):
        """
        Test that a negative input raises a RecursionError.
        A more robust implementation might raise a ValueError.
        """
        with self.assertRaises(RecursionError):
            factorial(-1)

    def test_non_integer_input(self):
        """Test that non-integer inputs raise appropriate errors."""
        with self.assertRaises(TypeError):
            factorial("a string")
        with self.assertRaises(RecursionError):
            factorial(2.5)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)