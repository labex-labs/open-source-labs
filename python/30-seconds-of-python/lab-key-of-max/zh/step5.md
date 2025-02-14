# 测试全为负值的情况

作为最后一个测试，让我们处理字典中所有值均为负数的情况。在 `TestKeyOfMax` 类中添加以下方法：

```python
    def test_all_negative_values(self):
        self.assertEqual(key_of_max({'x': -5, 'y': -2, 'z': -10}), 'y')
```

这个测试确保我们的函数能正确识别出 _负得最少_ 的值（在这种情况下即为最大值），并返回其关联的键。

最后再运行一次测试（`python3 test_key_of_max.py`）。所有四个测试都应该通过。这让我们有足够的信心认为我们的函数能正常工作。

你完整的 `test_key_of_max.py` 文件现在应该如下所示：

```python
import unittest
from key_of_max import key_of_max

class TestKeyOfMax(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(key_of_max({'a': 4, 'b': 0, 'c': 13}), 'c')

    def test_another_case(self):
        self.assertEqual(key_of_max({'apple': 10, 'banana': 5, 'orange': 10}), 'apple')

    def test_empty_dictionary(self):
        self.assertIsNone(key_of_max({}))

    def test_all_negative_values(self):
        self.assertEqual(key_of_max({'x': -5, 'y': -2, 'z': -10}), 'y')

if __name__ == '__main__':
    unittest.main()
```
