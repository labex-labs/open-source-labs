# 演習 8.1：単体テストの作成

別のファイル `test_stock.py` で、`Stock` クラスの単体テストのセットを書きます。始めに、インスタンス作成をテストする小さなコード断片を以下に示します。

```python
# test_stock.py

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

単体テストを実行します。以下のような出力が得られるはずです。

## .

Ran 1 tests in 0.000s

    OK

機能することが確認できたら、以下をチェックする追加の単体テストを書きます。

- `s.cost` プロパティが正しい値（49010.0）を返すことを確認する。
- `s.sell()` メソッドが正しく機能することを確認する。`s.shares` の値がそれに応じて減少する必要がある。
- `s.shares` 属性が整数以外の値に設定できないことを確認する。

最後の部分では、例外が発生することを確認する必要があります。それを行う簡単な方法は、以下のようなコードを使うことです。

```python
class TestStock(unittest.TestCase):
  ...
    def test_bad_shares(self):
         s = stock.Stock('GOOG', 100, 490.1)
         with self.assertRaises(TypeError):
             s.shares = '100'
```
