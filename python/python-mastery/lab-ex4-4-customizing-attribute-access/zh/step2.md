# 代理类

代理类是一种围绕现有类进行包装并提供相似接口的类。定义如下类，它为现有对象创建一个只读层：

```python
>>> class Readonly:
        def __init__(self, obj):
            self.__dict__['_obj'] = obj
        def __setattr__(self, name, value):
            raise AttributeError("Can't set attribute")
        def __getattr__(self, name):
            return getattr(self._obj, name)

>>>
```

要使用这个类，你只需将它围绕现有实例进行包装：

```python
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> p = Readonly(s)
>>> p.name
'GOOG'
>>> p.shares
100
>>> p.cost
49010.0
>>> p.shares = 50
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 8, in __setattr__
AttributeError: Can't set attribute
>>>
```
