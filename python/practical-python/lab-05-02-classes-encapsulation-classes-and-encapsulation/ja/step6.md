# 管理属性

一つのアプローチ：アクセサメソッドを導入する。

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.set_shares(shares)
        self.price = price

    # "取得" 操作を層化する関数
    def get_shares(self):
        return self._shares

    # "設定" 操作を層化する関数
    def set_shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        self._shares = value
```

残念ながら、これで既存のコードがすべて壊れてしまいます。`s.shares = 50` は `s.set_shares(50)` になります。
