# バリデータを使う

あなたのバリデータを使って、関数やクラスに値のチェックを追加することができます。たとえば、バリデータを `Stock` のプロパティに使うことができるかもしれません。

```python
class Stock:
  ...
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        self._shares = PositiveInteger.check(value)
  ...
```

`stock.py` から `Stock` クラスをコピーし、`shares` と `price` のプロパティコードでバリデータを使うように変更します。
