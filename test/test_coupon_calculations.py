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

    def test_price_under_between_ten_thirty(self):
        result1 = coupon_calculations.calculate_price(19.50, 5, 10)
        self.assertAlmostEquals(result1, 22.26, places=1)
        result1 = coupon_calculations.calculate_price(19.50, 5, 15)
        self.assertAlmostEquals(result1, 21.49, places=1)
        result1 = coupon_calculations.calculate_price(19.50, 5, 20)
        self.assertAlmostEquals(result1, 20.73, places=1)
        result1 = coupon_calculations.calculate_price(19.50, 10, 10)
        self.assertAlmostEquals(result1, 15.37, places=1)
        result1 = coupon_calculations.calculate_price(19.50, 10, 15)
        self.assertAlmostEquals(result1, 14.87, places=1)
        result1 = coupon_calculations.calculate_price(19.50, 10, 20)
        self.assertAlmostEquals(result1, 14.36, places=1)

    def test_price_under_between_thirty_fifty(self):
        result1 = coupon_calculations.calculate_price(49.50, 5, 10)
        self.assertAlmostEquals(result1, 55.12, places=1)
        result1 = coupon_calculations.calculate_price(49.50, 5, 15)
        self.assertAlmostEquals(result1, 52.77, places=1)
        result1 = coupon_calculations.calculate_price(49.50, 5, 20)
        self.assertAlmostEquals(result1, 50.40, places=1)
        result1 = coupon_calculations.calculate_price(49.50, 10, 10)
        self.assertAlmostEquals(result1, 50.35, places=1)
        result1 = coupon_calculations.calculate_price(49.50, 10, 15)
        self.assertAlmostEquals(result1, 48.26, places=1)
        result1 = coupon_calculations.calculate_price(49.50, 10, 20)
        self.assertAlmostEquals(result1, 46.16, places=1)

if __name__ == '__main__':
    unittest.main()
