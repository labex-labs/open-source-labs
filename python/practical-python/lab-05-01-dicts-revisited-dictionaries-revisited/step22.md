# Exercise 5.5: Inheritance

Make a new class that inherits from `Stock`.

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

Inheritance is implemented by extending the search process for attributes. The `__bases__` attribute has a tuple of the immediate parents:

```python
>>> NewStock.__bases__
(<class 'stock.Stock'>,)
>>>
```

The `__mro__` attribute has a tuple of all parents, in the order that they will be searched for attributes.

```python
>>> NewStock.__mro__
(<class '__main__.NewStock'>, <class 'stock.Stock'>, <class 'object'>)
>>>
```

Here's how the `cost()` method of instance `n` above would be found:

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
