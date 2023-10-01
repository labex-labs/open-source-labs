# Exercise 4.2: Adding some Methods

With classes, you can attach functions to your objects. These are known as methods and are functions that operate on the data stored inside an object. Add a `cost()` and `sell()` method to your `Stock` object. They should work like this:

```python
>>> import stock
>>> s = stock.Stock('GOOG', 100, 490.10)
>>> s.cost()
49010.0
>>> s.shares
100
>>> s.sell(25)
>>> s.shares
75
>>> s.cost()
36757.5
>>>
```  
