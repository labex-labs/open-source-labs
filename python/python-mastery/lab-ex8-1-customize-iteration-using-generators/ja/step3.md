# 反復処理の驚くべき力

Pythonは、予想外の方法で反復処理を使っています。`Structure` クラスに `__iter__()` を追加すると、あらゆる種類の新しい操作を簡単に行えるようになります。たとえば、シーケンスへの変換とアンパッキングです：

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> list(s)
['GOOG', 100, 490.1]
>>> tuple(s)
('GOOG', 100, 490.1)
>>> name, shares, price = s
>>> name
'GOOG'
>>> shares
100
>>> price
490.1
>>>
```

ここでやっている最中に、`Structure` クラスに比較演算子を追加することができます：

```python
# structure.py
class Structure(metaclass=StructureMeta):
 ...
    def __eq__(self, other):
        return isinstance(other, type(self)) and tuple(self) == tuple(other)
 ...
```

これで、オブジェクトを比較できるようになります：

```python
>>> a = Stock('GOOG', 100, 490.1)
>>> b = Stock('GOOG', 100, 490.1)
>>> a == b
True
>>>
```

もう一度 `teststock.py` のユニットテストを実行してみてください。今ではすべてが合格するはずです。素晴らしいです。
