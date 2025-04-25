# format() メソッド

引数またはキーワード引数に書式設定を適用できる`format()`メソッドがあります。

```python
>>> '{name:>10s} {shares:10d} {price:10.2f}'.format(name='IBM', shares=100, price=91.1)
'       IBM        100      91.10'
>>> '{:>10s} {:10d} {:10.2f}'.format('IBM', 100, 91.1)
'       IBM        100      91.10'
>>>
```

正直なところ、`format()`は少し冗長です。私は f-文字列の方が好きです。
