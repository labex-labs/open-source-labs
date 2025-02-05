# 绑定方法

这可能会让人惊讶，但方法调用是建立在用于简单属性的机制之上的。本质上，方法是一种属性，当你像调用函数一样添加所需的括号（）来调用它时，它就会执行。例如：

```python
>>> s = Stock('GOOG',100,490.10)
>>> s.cost           # 查找方法
<bound method Stock.cost of <__main__.Stock object at 0x409530>>
>>> s.cost()         # 查找并调用方法
49010.0

>>> # 使用 getattr() 的相同操作
>>> getattr(s, 'cost')
<bound method Stock.cost of <__main__.Stock object at 0x409530>>
>>> getattr(s, 'cost')()
49010.0
>>>
```

绑定方法与它所属的对象相关联。如果该对象被修改，方法将看到这些修改。你可以通过检查方法的 `__self__` 属性来查看原始对象。

```python
>>> c = s.cost
>>> c()
49010.0
>>> s.shares = 75
>>> c()
36757.5
>>> c.__self__
<__main__.Stock object at 0x409530>
>>> c.__func__
<function cost at 0x37cc30>
>>> c.__func__(c.__self__)      # 这是调用 c() 时幕后发生的事情
36757.5
>>>
```

用 `sell()` 方法试试，以确保你理解其中的原理：

```python
>>> f = s.sell
>>> f.__func__(f.__self__, 25)     # 等同于 s.sell(25)
>>> s.shares
50
>>>
```
