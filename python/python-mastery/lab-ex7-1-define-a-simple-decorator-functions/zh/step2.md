# 一个真正的装饰器

提示：在`validate.py`文件中完成以下内容

在练习6.6中，你创建了一个可调用类`ValidatedFunction`来强制实施类型注释。将这个类重写为一个名为`validated`的装饰器函数。它应该允许你编写如下代码：

```python
from validate import Integer, validated

@validated
def add(x: Integer, y:Integer) -> Integer:
    return x + y

@validated
def pow(x: Integer, y:Integer) -> Integer:
    return x ** y
```

以下是装饰后的函数应有的工作方式：

```python
>>> add(2, 3)
5
>>> add('2', '3')
追溯（最近一次调用）：
  文件 "<stdin>"，第1行，在 <模块> 中
  文件 "validate.py"，第75行，在 wrapper 中
    引发 TypeError('参数错误\n' + '\n'.join(errors))
TypeError：参数错误
    x：期望为 <class 'int'>
    y：期望为 <class 'int'>

>>> pow(2, 3)
8
>>> pow(2, -1)
追溯（最近一次调用）：
  文件 "<stdin>"，第1行，在 <模块> 中
  文件 "validate.py"，第83行，在 wrapper 中
    引发 TypeError(f'返回错误：{e}') 从 None
TypeError：返回错误：期望为 <class 'int'>
>>>
```

你的装饰器应该尝试处理异常，以便它们能显示更有用的信息，如上述所示。此外，`@validated`装饰器在类中也应该能正常工作（你不需要做任何特别的事情）。

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @validated
    def sell(self, nshares:PositiveInteger):
        self.shares -= nshares
```

注意：这部分不需要很多代码，但有很多底层的琐碎细节。解决方案看起来与练习6.6的几乎一样。不过，不要不好意思查看解决方案代码。
