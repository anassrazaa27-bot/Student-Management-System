import unittest
from src.grading import calculate_grade

class TestGrading(unittest.TestCase):
    def test_grade_boundaries(self):
        self.assertEqual(calculate_grade(95), "A+")
        self.assertEqual(calculate_grade(85), "A")
        self.assertEqual(calculate_grade(75), "B")
        self.assertEqual(calculate_grade(65), "C")
        self.assertEqual(calculate_grade(55), "D")
        self.assertEqual(calculate_grade(40), "F")

    def test_invalid_average(self):
        with self.assertRaises(ValueError):
            calculate_grade(101)
        with self.assertRaises(ValueError):
            calculate_grade(-1)

if __name__ == "__main__":
    unittest.main()
