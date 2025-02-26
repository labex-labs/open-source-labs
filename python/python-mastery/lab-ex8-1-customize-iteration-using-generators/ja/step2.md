# オブジェクトに反復処理を追加する

カスタムクラスを作成した場合、`__iter__()` という特殊メソッドを定義することで反復処理をサポートさせることができます。`__iter__()` は結果としてイテレータを返します。前の例で示したように、簡単な方法は `__iter__()` をジェネレータとして定義することです。

以前のエクササイズで、`Structure` というベースクラスを定義しました。このクラスに、属性値を順番に生成する `__iter__()` メソッドを追加しましょう。たとえば：

```python
class Structure(metaclass=StructureMeta):
  ...
    def __iter__(self):
        for name in self._fields:
            yield getattr(self, name)
  ...
```

これを行ったら、インスタンス属性を次のように反復処理できるはずです：

```python
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> for val in s:
        print(val)
GOOG
100
490.1
>>>
```
