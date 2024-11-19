import unittest
from area import calculate_rectangle_area, calculate_triangle_area, calculate_circle_area

class TestAreaFunctions(unittest.TestCase):
    def test_calculate_rectangle_area(self):
        self.assertEqual(calculate_rectangle_area(5, 10), 50)
        self.assertEqual(calculate_rectangle_area(3, 7), 21)

    def test_calculate_triangle_area(self):
        self.assertEqual(calculate_triangle_area(5, 10), 25)
        self.assertEqual(calculate_triangle_area(4, 6), 12)

    def test_calculate_circle_area(self):
        self.assertEqual(calculate_circle_area(3), 28.274333882308138)  # pi * r^2
        self.assertEqual(calculate_circle_area(5), 78.53981633974483)

if __name__ == '__main__':
    unittest.main()
