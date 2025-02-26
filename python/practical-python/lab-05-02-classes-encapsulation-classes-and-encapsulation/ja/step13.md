# 演習5.7：プロパティとセッター

`shares` 属性を変更して、値をプライベート属性に格納し、常に整数値に設定されるようにするための一対のプロパティ関数を使用します。期待される動作の例は次のとおりです。

```python
>>> ================================ RESTART ================================
>>> from stock import Stock
>>> s = Stock('GOOG',100,490.10)
>>> s.shares = 50
>>> s.shares = 'a lot'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: expected an integer
>>>
```
