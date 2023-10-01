#!/bin/zsh
import sys


sys.path.append('/home/labex/project')
import pcost
import report
import unittest

class TestScripts(unittest.TestCase):
    def test_main_methods(self):
        
        pcost_result = pcost.main(['/home/labex/project/pcost.py', '/home/labex/project/portfolio.csv'])
        pcost_expected_output = 'Total cost: 44671.15'
        self.assertEqual(pcost_result, pcost_expected_output)

        
        report_result = report.main(['/home/labex/project/report.py', '/home/labex/project/portfolio.csv', '/home/labex/project/prices.csv'])
        report_expected_substring = "Name"
        self.assertIn(report_expected_substring, report_result)

if __name__ == '__main__':
    unittest.main()