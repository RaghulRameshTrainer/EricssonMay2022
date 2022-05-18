import unittest
from circles import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(1),pi)
        self.assertEqual(circle_area(0),0)
        self.assertAlmostEqual(circle_area(1.21),pi*1.21*1.21)
    def test_values(self):
        self.assertRaises(ValueError,circle_area,-3)
    def test_types(self):
        self.assertRaises(TypeError, circle_area, 2+3j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "Chennai")
    # def test_result(self):
    #     self.assertRaises(ValueError,circle_area,0)