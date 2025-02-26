# `__slots__` の追加

新しい `Stock` クラスを変更して `__slots__` を使用するようにします。以前とは異なる属性名のセットを使用する必要があることに気付くでしょう。具体的には、プライベート属性名をリストする必要があります（たとえば、プロパティが属性 `_shares` に値を格納している場合、それが `__slots__` にリストする名前です）。クラスがまだ機能し、新しい属性を追加できなくなったことを確認します。

```python
>>> s = Stock('GOOG', 100, 490.10)
>>> s.spam = 42
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Stock' object has no attribute 'spam'
>>>
```
