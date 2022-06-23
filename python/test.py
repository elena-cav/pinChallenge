import unittest

from index import generateResult


class TestPinsGenerator(unittest.TestCase):
    def test_num(self):
        """
        Test that it can find all combinations when given one digit
        """
        result = generateResult(1)
        self.assertEqual(result, [1, 2, 4])

    # def test_bottom_row(self):
    #     """
    #     Test that it can
    #     """
    #     result = generateResult(46)
    #     self.assertEqual(result, [
    #         55, 15, 75, 45, 53, 13, 56, 16, 59, 19, 73, 43, 76, 46, 79, 49,
    #     ])


if __name__ == '__main__':
    unittest.main()
