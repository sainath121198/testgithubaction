import unittest
from src import math_ops


class TestMathOps(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(math_ops.add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(math_ops.add(-1, -1), -2)

    def test_multiply(self):
        self.assertEqual(math_ops.multiply(3, 4), 12)


if __name__ == '__main__':
    unittest.main()
