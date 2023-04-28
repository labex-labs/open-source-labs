import unittest
from hex_to_rgb import *

def hex_to_rgb(hex):
  return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

class TestHexToRgb(unittest.TestCase):
  
  def test_hex_to_rgb(self):
    self.assertEqual(hex_to_rgb("FF0000"), (255, 0, 0))
    self.assertEqual(hex_to_rgb("00FF00"), (0, 255, 0))
    self.assertEqual(hex_to_rgb("0000FF"), (0, 0, 255))
    self.assertEqual(hex_to_rgb("FFFFFF"), (255, 255, 255))
    self.assertEqual(hex_to_rgb("000000"), (0, 0, 0))
    
if __name__ == '__main__':
  unittest.main()