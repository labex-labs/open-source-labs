# Exercise 5.6: Simple Properties

Properties are a useful way to add "computed attributes" to an object. In `stock.py`, you created an object `Stock`. Notice that on your object there is a slight inconsistency in how different kinds of data are extracted:

```python
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> s.shares
100
>>> s.price
490.1
>>> s.cost()
49010.0
>>>
```

Specifically, notice how you have to add the extra () to `cost` because it is a method.

You can get rid of the extra () on `cost()` if you turn it into a property. Take your `Stock` class and modify it so that the cost calculation works like this:

```python
>>> ================================ RESTART ================================
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> s.cost
49010.0
>>>
```

Try calling `s.cost()` as a function and observe that it doesn't work now that `cost` has been defined as a property.

```python
>>> s.cost()
... fails ...
>>>
```

Making this change will likely break your earlier `pcost.py` program. You might need to go back and get rid of the `()` on the `cost()` method.
