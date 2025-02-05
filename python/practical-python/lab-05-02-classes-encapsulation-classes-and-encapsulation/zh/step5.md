# 简单属性

考虑以下类。

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

一个令人惊讶的特性是，你可以将属性设置为任何值：

```python
>>> s = Stock('IBM', 50, 91.1)
>>> s.shares = 100
>>> s.shares = "hundred"
>>> s.shares = [1, 0, 0]
>>>
```

你可能会看到这种情况并认为需要一些额外的检查。

```python
s.shares = '50'     # 引发 TypeError，这是一个字符串
```

你会怎么做呢？
