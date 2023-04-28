import unittest
from merge import *

def merge(*args, fill_value=None):
    max_length = max([len(lst) for lst in args])
    result = []
    for i in range(max_length):
        result.append([
            args[k][i] if i < len(args[k]) else fill_value for k in range(len(args))
        ])
    return result

class TestMerge(unittest.TestCase):
    def test_merge(self):
        self.assertEqual(merge([1, 2, 3], [4, 5, 6], [7, 8, 9]), [[1, 4, 7], [2, 5, 8], [3, 6, 9]])
        self.assertEqual(merge([1, 2], [3, 4, 5], [6]), [[1, 3, 6], [2, 4, None], [None, 5, None]])
        self.assertEqual(merge([1, 2, 3], [4, 5], [6, 7, 8], fill_value=0), [[1, 4, 6], [2, 5, 7], [3, 0, 8]])

if __name__ == '__main__':
    unittest.main()