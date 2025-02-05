# 练习 5.5：继承

创建一个从 `Stock` 类继承的新类。

```python
>>> class NewStock(Stock):
        def yow(self):
            print('Yow!')

>>> n = NewStock('ACME', 50, 123.45)
>>> n.cost()
6172.50
>>> n.yow()
Yow!
>>>
```

继承是通过扩展属性搜索过程来实现的。`__bases__` 属性包含一个直接父类的元组：

```python
>>> NewStock.__bases__
(<class 'stock.Stock'>,)
>>>
```

`__mro__` 属性包含所有父类的元组，按照搜索属性的顺序排列。

```python
>>> NewStock.__mro__
(<class '__main__.NewStock'>, <class 'stock.Stock'>, <class 'object'>)
>>>
```

下面展示了如何找到上述实例 `n` 的 `cost()` 方法：

```python
>>> for cls in n.__class__.__mro__:
        if 'cost' in cls.__dict__:
            break

>>> cls
<class '__main__.Stock'>
>>> cls.__dict__['cost']
<function cost at 0x101aed598>
>>>
```
