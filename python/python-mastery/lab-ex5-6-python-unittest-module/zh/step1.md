# 准备工作

在之前的实验中，你创建了一个包含`Stock`类的`stock.py`文件。在另一个名为`teststock.py`的文件中，定义以下测试代码：

```python
# teststock.py

import unittest
import stock

class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

if __name__ == '__main__':
    unittest.main()
```

确保你能够运行该文件：

````bash
python3 teststock.py
.
------------------------------------------------------------------```
Ran 1 tests in 0.001s

OK
````
