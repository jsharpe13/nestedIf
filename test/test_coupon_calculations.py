import unittest
from store import coupon_calculations


class FunctionTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        result1 = coupon_calculations.calculate_price(9.50, 5, 10)
        self.assertAlmostEquals(result1, 10.60, places=1)
        result1 = coupon_calculations.calculate_price(9.50, 5, 15)
        self.assertAlmostEquals(result1, 10.36, places=1)
        result1 = coupon_calculations.calculate_price(9.50, 5, 20)
        self.assertAlmostEquals(result1, 10.12, places=1)
        result1 = coupon_calculations.calculate_price(9.50, 10, 10)
        self.assertAlmostEquals(result1, 5.83, places=1)
        result1 = coupon_calculations.calculate_price(9.50, 10, 15)
        self.assertAlmostEquals(result1, 5.85, places=1)
        result1 = coupon_calculations.calculate_price(9.50, 10, 20)
        self.assertAlmostEquals(result1, 5.88, places=1)

if __name__ == '__main__':
    unittest.main()
