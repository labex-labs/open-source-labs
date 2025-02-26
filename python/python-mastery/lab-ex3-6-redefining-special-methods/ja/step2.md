# オブジェクトを比較可能にする

同じ`Stock`オブジェクトを2つ作成して比較しようとするとどうなるかを調べましょう。

```python
>>> a = Stock('GOOG', 100, 490.1)
>>> b = Stock('GOOG', 100, 490.1)
>>> a == b
False
>>>
```

これを修正するには、`Stock`クラスに`__eq__()`メソッドを与えます。たとえば：

```python
class Stock:
  ...
    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                             (other.name, other.shares, other.price))
  ...
```

この変更を行って、再度2つのオブジェクトを比較してみましょう。
