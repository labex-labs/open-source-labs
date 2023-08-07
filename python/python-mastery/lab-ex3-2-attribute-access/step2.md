# Using getattr()

The `getattr()` function is extremely useful for writing code that processes objects in an extremely generic way. To illustrate, consider this example which prints out a set of user-defined attributes:

```python
>>> s= Stock('GOOG', 100, 490.1)
>>> fields = ['name','shares','price']
>>> for name in fields:
           print(name, getattr(s, name))

name GOOG
shares 100
price 490.1
>>>
```
