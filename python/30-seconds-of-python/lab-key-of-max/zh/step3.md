# 创建单元测试：基础测试

现在，让我们编写一些测试，以确保我们的函数能正确工作。我们将使用 Python 的 `unittest` 模块。创建一个名为 `test_key_of_max.py` 的新文件，并添加以下代码：

```python
import unittest
from key_of_max import key_of_max  # Import our function

class TestKeyOfMax(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(key_of_max({'a': 4, 'b': 0, 'c': 13}), 'c')

    def test_another_case(self):
        self.assertEqual(key_of_max({'apple': 10, 'banana': 5, 'orange': 10}), 'apple')

if __name__ == '__main__':
    unittest.main()
```

解释：

1. **`import unittest`**：导入测试框架。
2. **`from key_of_max import key_of_max`**：导入我们要测试的函数。
3. **`class TestKeyOfMax(unittest.TestCase):`**：定义一个 _测试类_。测试类将相关的测试组合在一起。
4. **`def test_basic_case(self):`**：定义一个 _测试方法_。每个测试方法检查我们函数的一个特定方面。测试方法的名称 _必须_ 以 `test_` 开头。
5. **`self.assertEqual(...)`**：这是一个 _断言_。它检查两个值是否相等。如果它们不相等，测试就会失败。在这种情况下，我们检查 `key_of_max({'a': 4, 'b': 0, 'c': 13})` 是否返回 `'c'`，它应该返回这个值。
6. **`def test_another_case(self):`**：添加另一个测试用例，以验证最大值对应的键可能不唯一的情况。
7. **`if __name__ == '__main__': unittest.main()`**：这是标准的 Python 惯用法，当你直接执行脚本时（例如 `python3 test_key_of_max.py`），它会运行测试。

从终端运行测试：`python3 test_key_of_max.py`。你应该会看到输出，表明这两个测试都通过了。

```python
python3 test_key_of_max.py
```

```plaintext
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
