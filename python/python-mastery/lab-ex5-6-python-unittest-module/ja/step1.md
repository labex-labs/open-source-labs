# 準備

以前の演習では、`Stock` クラスを含む `stock.py` というファイルを作成しました。別のファイルである `teststock.py` に、次のテストコードを定義します。

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

このファイルを実行できることを確認しましょう。

````bash
python3 teststock.py
.
------------------------------------------------------------------```
Ran 1 tests in 0.001s

OK
````
