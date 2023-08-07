# Method Invocation

Invoking a method is a two-step process.

1.  Lookup: The `.` operator
2.  Method call: The `()` operator

```python
>>> s = Stock('GOOG',100,490.10)
>>> c = s.cost  # Lookup
>>> c
<bound method Stock.cost of <Stock object at 0x590d0>>
>>> c()         # Method call
49010.0
>>>
```
