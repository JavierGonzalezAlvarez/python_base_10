import unittest
from challenge import count_integer_digits

class TestNumber(unittest.TestCase):
    '''class for tests'''

    def test_number1(self):
        '''test2'''
        result1: int | float = count_integer_digits(100)
        self.assertEqual(result1, 3, "Should be 3")

    def test_number2(self):
        '''test2'''
        result: int | float = count_integer_digits(999)
        self.assertEqual(result, 3, "Should be 3")

    def test_number3(self):
        '''test3'''
        result: int | float = count_integer_digits(10)
        self.assertEqual(result, 2, "Should be 2")

    def test_number4(self):
        '''test4'''
        result: int | float = count_integer_digits(3.1415)
        self.assertEqual(result, 1, "Should be 1")

    def test_number5(self):
        '''test5'''
        result: int | float = count_integer_digits(0)
        self.assertEqual(result, 1, "Should be 1")

    def test_number6(self):
        '''test6'''
        result: int | float = count_integer_digits("hello world")
        self.assertFalse(isinstance(result, (int, float)), "Should be integer or float type")

if __name__ == '__main__':
    unittest.main()

