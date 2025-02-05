# 实际应用中的描述符

之前，你创建了一个`Stock`类，它使用了插槽、属性和其他特性。所有这些特性都是通过描述符协议来实现的。通过这个简单的实验来看看它的实际应用。

首先，创建一个股票对象，并尝试查找一些属性：

```python
>>> s = Stock('GOOG', 100, 490.10)
>>> s.name
'GOOG'
>>> s.shares
100
>>>
```

现在，注意这些属性在类字典中。

```python
>>> Stock.__dict__.keys()
['sell', '__module__', '__weakref__', 'price', '_price','shares', '_shares',
'__slots__', 'cost', '__repr__', '__doc__', '__init__']
>>>
```

尝试以下步骤，这些步骤说明了描述符如何在实例上获取和设置值：

```python
>>> q = Stock.__dict__['shares']
>>> q.__get__(s)
100
>>> q.__set__(s,75)
>>> s.shares
75
>>> q.__set__(s, '75')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "stock.py", line 23, in shares
    raise TypeError('Expected an integer')
TypeError: 预期为整数
>>>
```

每当你访问实例时，`__get__()`和`__set__()`的执行会自动发生。
