# `unittest` 模块

假设你在 `simple.py` 中有一些代码。

```python
# simple.py

def add(x, y):
    return x + y
```

现在，假设你想要测试它。在 `/home/labex/project/test_simple.py` 中创建一个单独的测试文件，如下所示。

```python
# test_simple.py

import simple
import unittest
```

然后定义一个测试类。

```python
# test_simple.py

import simple
import unittest

# 注意它继承自 unittest.TestCase
class TestAdd(unittest.TestCase):
  ...
```

测试类必须继承自 `unittest.TestCase`。

在测试类中，你定义测试方法。

```python
# test_simple.py

import simple
import unittest

# 注意它继承自 unittest.TestCase
class TestAdd(unittest.TestCase):
    def test_simple(self):
        # 用简单整数参数进行测试
        r = simple.add(2, 2)
        self.assertEqual(r, 5)
    def test_str(self):
        # 用字符串进行测试
        r = simple.add('hello', 'world')
        self.assertEqual(r, 'helloworld')
```

\*重要提示：每个方法都必须以 `test` 开头。
