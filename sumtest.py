import unittest
from addition import add_nums


class SumTest(unittest.TestCase):
    def test_nums(self):
        self.assertEqual(add_nums(10,20),30)
        self.assertEqual(add_nums(10,-10),0)
    def test_nums(self):
        self.assertRaises(TypeError,add_nums,10)