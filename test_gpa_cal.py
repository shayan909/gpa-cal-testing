import unittest
from unittest import TestCase

import gpa_cal


class Test1(TestCase):
    # tests empty inputs
    def test_type_error(self):
        gradePoints, credits = gpa_cal.courses()

        self.assertNotIn('', gradePoints)
        self.assertNotIn('', credits)


class Test5(TestCase):

    # tests correct output
    def test_gpa(self):
        credits = [3, 3, 3, 3, 3]  # 10 Cr/hr
        gradePoints = [3, 3.5, 3, 3.25, 3]  # weightage  = 3.4
        self.assertAlmostEqual(gpa_cal.gpa_cal(gradePoints, credits), 3.9)


# test no. of courses <=0
class Test2(TestCase):
    def test_courses(self):
        self.assertRaises(ValueError, gpa_cal.courses)


if __name__ == '__main__':
    unittest.main()
