# format() 方法

有一个 `format()` 方法，它可以对参数或关键字参数应用格式化。

```python
>>> '{name:>10s} {shares:10d} {price:10.2f}'.format(name='IBM', shares=100, price=91.1)
'       IBM        100      91.10'
>>> '{:>10s} {:10d} {:10.2f}'.format('IBM', 100, 91.1)
'       IBM        100      91.10'
>>>
```

坦率地说，`format()` 有点冗长。我更喜欢 f 字符串。
