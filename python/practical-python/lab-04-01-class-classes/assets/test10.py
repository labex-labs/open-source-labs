import sys


sys.path.append('/home/labex/project')

import unittest
import pcost
import report

class TestPortfolio(unittest.TestCase):
    def test_portfolio_cost(self):
        cost = pcost.portfolio_cost('/home/labex/project/portfolio.csv')
        self.assertEqual(cost, 44671.15)

    def test_portfolio_report(self):
        expected_substring = "Name"

        report_output = report.portfolio_report('/home/labex/project/portfolio.csv', '/home/labex/project/prices.csv')
        self.assertIn(expected_substring, report_output)

if __name__ == '__main__':
    unittest.main()