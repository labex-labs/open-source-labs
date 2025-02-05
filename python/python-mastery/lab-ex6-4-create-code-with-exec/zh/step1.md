# 使用 exec() 进行实验

在字符串中定义一段 Python 代码片段并尝试运行它：

```python
>>> code = '''
for i in range(n):
    print(i, end=' ')
'''
>>> n = 10
>>> exec(code)
0 1 2 3 4 5 6 7 8 9
>>>
```

这很有趣，但执行随机的代码片段并没有特别大的用处。`exec()` 更有趣的用途是用于创建诸如函数、方法或类之类的代码。试试这个例子，我们为一个类创建一个 `__init__()` 函数。

```python
>>> class Stock:
        _fields = ('name','shares', 'price')

>>> argstr = ','.join(Stock._fields)
>>> code = f'def __init__(self, {argstr}):\n'
>>> for name in Stock._fields:
        code += f'    self.{name} = {name}\n'
>>> print(code)
def __init__(self, name,shares,price):
    self.name = name
    self.shares = shares
    self.price = price

>>> locs = { }
>>> exec(code, locs)
>>> Stock.__init__ = locs['__init__']

>>> # 现在试试这个类
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
>>>
```

在这个例子中，直接根据 `_fields` 变量创建了一个 `__init__()` 函数。这里没有涉及特殊的 `_init()` 方法或栈帧的奇怪技巧。
