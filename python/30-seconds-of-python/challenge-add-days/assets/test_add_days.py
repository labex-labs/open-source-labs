import unittest
import sys
sys.path.append("/home/labex/project")
from add_days import *

from datetime import datetime, timedelta

class TestAddDays(unittest.TestCase):
    
    def test_add_days(self):
        self.assertEqual(add_days(1, datetime(2022, 1, 1)), datetime(2022, 1, 2))
        self.assertEqual(add_days(7, datetime(2022, 1, 1)), datetime(2022, 1, 8))
        
if __name__ == '__main__':
    unittest.main()