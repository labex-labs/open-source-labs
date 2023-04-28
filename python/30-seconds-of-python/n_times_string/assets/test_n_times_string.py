import unittest
from n_times_string import *

class TestNTimesString(unittest.TestCase):
    
    def test_n_times_string(self):
        self.assertEqual(n_times_string("hello", 3), "hellohellohello")
        self.assertEqual(n_times_string("abc", 0), "")
        self.assertEqual(n_times_string("xyz", 5), "xyzxyzxyzxyzxyz")
        self.assertEqual(n_times_string("", 10), "")