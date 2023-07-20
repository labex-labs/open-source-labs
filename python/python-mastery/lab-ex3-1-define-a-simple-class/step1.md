# Adding a new method

Add a new method `sell(nshares)` to Stock that sells a certain number
of shares by decrementing the share count. Have it work like this:

```python
>>> s = Stock('GOOG',100,490.10)
>>> s.shares
100
>>> s.sell(25)
>>> s.shares
75
>>>
```
