#!/bin/bash
# Create a test file for verification
cat > /tmp/test_months_diff.py << 'EOL'
import unittest
from datetime import date
from math import ceil

def months_diff(start, end):
    return ceil((end - start).days / 30)

class TestMonthsDiff(unittest.TestCase):
    def test_same_month(self):
        self.assertEqual(months_diff(date(2020, 10, 1), date(2020, 10, 25)), 1)
        
    def test_consecutive_months(self):
        self.assertEqual(months_diff(date(2020, 10, 28), date(2020, 11, 25)), 1)
        
    def test_across_year(self):
        self.assertEqual(months_diff(date(2020, 12, 15), date(2021, 1, 10)), 1)
        
    def test_several_months(self):
        self.assertEqual(months_diff(date(2020, 5, 1), date(2020, 8, 15)), 4)
        
    def test_negative_result(self):
        self.assertEqual(months_diff(date(2020, 8, 15), date(2020, 5, 1)), -3)

if __name__ == '__main__':
    unittest.main()
EOL

chmod +x /tmp/test_months_diff.py
