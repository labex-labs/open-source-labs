# Exercise 5.7: Properties and Setters

Modify the `shares` attribute so that the value is stored in a
private attribute and that a pair of property functions are used to ensure
that it is always set to an integer value. Here is an example of the expected
behavior:

```python
>>> ================================ RESTART ================================
>>> from stock import Stock
>>> s = Stock('GOOG',100,490.10)
>>> s.shares = 50
>>> s.shares = 'a lot'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: expected an integer
>>>
```
