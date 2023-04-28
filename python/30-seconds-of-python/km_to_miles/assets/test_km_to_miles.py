import unittest
import sys
sys.path.append("/home/labex/project")
from km_to_miles import *

class TestKmToMiles(unittest.TestCase):
    def test_km_to_miles(self):
        self.assertAlmostEqual(km_to_miles(1), 0.621371)
        self.assertAlmostEqual(km_to_miles(5), 3.106855)
        self.assertAlmostEqual(km_to_miles(10), 6.21371)
        
if __name__ == '__main__':
    unittest.main()