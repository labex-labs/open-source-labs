# 用作方法（挑战）

如果将自定义可调用对象用作自定义方法，通常会出现问题。例如，试试这个：

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares:Integer):
        self.shares -= nshares
    sell = ValidatedFunction(sell)     # 失败
```

你会发现包装后的`sell()`严重失败：

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.sell(10)
Traceback (最近一次调用最后):
  File "<stdin>", line 1, in <module>
  File "validate.py", line 64, in __call__
    bound = self.signature.bind(*args, **kwargs)
  File "/usr/local/lib/python3.6/inspect.py", line 2933, in bind
    return args[0]._bind(args[1:], kwargs)
  File "/usr/local/lib/python3.6/inspect.py", line 2848, in _bind
    raise TypeError(msg) from None
TypeError: 缺少一个必需的参数: 'nshares'
>>>
```

奖励：弄清楚它为什么失败——但不要在这上面花太多时间瞎折腾。
