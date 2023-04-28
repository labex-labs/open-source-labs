import unittest
from find_parity_outliers import *


class TestFindParityOutliers(unittest.TestCase):
  
  def test_find_parity_outliers(self):
    self.assertEqual(find_parity_outliers([1,2,3,4,5]), [2,4])
    self.assertEqual(find_parity_outliers([1,3,5,7,9]), [])
    self.assertEqual(find_parity_outliers([2,4,6,8,10]), [])
    self.assertEqual(find_parity_outliers([1,1,1,1,2]), [2])
    self.assertEqual(find_parity_outliers([1,1,1,1,1]), [])
    
if __name__ == '__main__':
  unittest.main()