# カスタム単位クラスの作成

このステップでは、カスタム単位クラス - `Foo` を作成します。このクラスは、「単位」に応じて変換と異なる目盛りの書式設定をサポートします。ここでの「単位」は、単なるスカラー変換係数です。

```python
class Foo:
    def __init__(self, val, unit=1.0):
        self.unit = unit
        self._val = val * unit

    def value(self, unit):
        if unit is None:
            unit = self.unit
        return self._val / unit
```
