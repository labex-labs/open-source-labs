# 行の変換

`Structure` クラスには欠けている機能の1つが、より古いCSV読み取りコードと連携するための `from_row()` メソッドです。これを修正しましょう。`Structure` クラスに `_types` というクラス変数と次のクラスメソッドを追加します。

```python
# structure.py

class Structure:
    _types = ()
 ...
    @classmethod
    def from_row(cls, row):
        rowdata = [ func(val) for func, val in zip(cls._types, row) ]
        return cls(*rowdata)
 ...
```

`@validate_attributes` デコレータを変更して、それが `expected_type` 属性を持つさまざまなバリデータを調べ、それを使って上記の `_types` 変数を埋めるようにします。

これを行ったら、次のようなことができるようになります。

```python
>>> s = Stock.from_row(['GOOG', '100', '490.1'])
>>> s
Stock('GOOG', 100, 490.1)
>>> import reader
>>> port = reader.read_csv_as_instances('portfolio.csv', Stock)
>>>
```
