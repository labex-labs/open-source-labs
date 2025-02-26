# 検証ルールの強制

プロパティとプライベート属性を使用して、`Stock` クラスの `shares` 属性を変更して、非負の整数値のみを割り当てることができるようにします。また、`price` 属性を変更して、非負の浮動小数点数値のみを割り当てることができるようにします。

新しいオブジェクトは、追加の型と値のチェックを除いて、古いオブジェクトとほぼ同じように機能する必要があります。

```python
>>> s = Stock('GOOG', 100, 490.10)
>>> s.shares = 50          # 正常
>>> s.shares = '50'
Traceback (most recent call last):
...
TypeError: 整数が必要です
>>> s.shares = -10
Traceback (most recent call last):
...
ValueError: shares は 0 以上でなければなりません

>>> s.price = 123.45       # 正常
>>> s.price = '123.45'
Traceback (most recent call last):
...
TypeError: 浮動小数点数が必要です
>>> s.price = -10.0
Traceback (most recent call last):
...
ValueError: price は 0 以上でなければなりません
>>>
```
