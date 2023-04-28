import unittest
from miles_to_km import *

class TestMilesToKm(unittest.TestCase):
    
    def test_miles_to_km(self):
        self.assertEqual(miles_to_km(0), 0.0)
        self.assertEqual(miles_to_km(1), 1.609344)
        self.assertEqual(miles_to_km(10), 16.09344)
        self.assertEqual(miles_to_km(100), 160.9344)
        self.assertEqual(miles_to_km(-1), -1.609344)
        
if __name__ == '__main__':
    unittest.main()