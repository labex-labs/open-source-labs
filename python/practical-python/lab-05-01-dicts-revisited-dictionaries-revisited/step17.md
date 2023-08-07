# Some Cautions

Multiple inheritance is a powerful tool. Remember that with power comes responsibility. Frameworks / libraries sometimes use it for advanced features involving composition of components. Now, forget that you saw that.

In Section 4, you defined a class `Stock` that represented a holding of stock. In this exercise, we will use that class. Restart the interpreter and make a few instances:

```python
>>> ================================ RESTART ================================
>>> from stock import Stock
>>> goog = Stock('GOOG',100,490.10)
>>> ibm  = Stock('IBM',50, 91.23)
>>>
```
