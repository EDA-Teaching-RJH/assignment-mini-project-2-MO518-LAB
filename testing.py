import unittest

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

class TestMathOperations(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5) # test with positive integers
        self.assertEqual(add_numbers(0, 0), 0) # test with zero
        self.assertEqual(add_numbers(-1, 3), 2) # test with positive and negative integers
        self.assertEqual(add_numbers(2.5, 2.2), 3.5) # test with floats

    def test_subtract_numbers(self):
        self.assertEqual(subtract_numbers(5, 3), 2)  # Test with positive integers
        self.assertEqual(subtract_numbers(-1, 1), -2)  # Test with a negative and positive number
        self.assertEqual(subtract_numbers(0, 0), 0)  # Test with zero
        self.assertAlmostEqual(subtract_numbers(5.5, 2.2), 3.3)  # Test with floats

# Main block to run tests
if __name__ == '__main__':
    unittest.main()
