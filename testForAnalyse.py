import unittest
import bisection_secant_newthon_raphson


class BisectionWithSecant(unittest.TestCase):
    def test_tow_method(self):
        self.assertAlmostEqual(bisection_secant_newthon_raphson.bisection(
            lambda x: x ** 3 - x - 2, 1, 2), bisection_secant_newthon_raphson.secant(
            lambda x: x ** 3 - x - 2, 30, 10), True)


if __name__ == '__main__':
    pass
# code
