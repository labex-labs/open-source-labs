# Method Resolution Order or MRO

Python precomputes an inheritance chain and stores it in the _MRO_ attribute on the class. You can view it.

```python
>>> E.__mro__
(<class '__main__.E'>, <class '__main__.D'>,
 <class '__main__.B'>, <class '__main__.A'>,
 <type 'object'>)
>>>
```

This chain is called the **Method Resolution Order**. To find an attribute, Python walks the MRO in order. The first match wins.
