# Properties for computed attributes

Earlier, you defined a class `Stock`. For example:

```python
>>> s = Stock('GOOG',100,490.10)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
>>> s.cost()
49010.0
>>>
```

Using a property, turn `cost()` into an attribute that no longer requires the parentheses. For example:

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.cost               # Property. Computes the cost
49010.0
>>>
```
