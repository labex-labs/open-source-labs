# How inheritance works

Classes may inherit from other classes.

```python
class A(B, C):
    ...
```

The base classes are stored in a tuple in each class.

```python
>>> A.__bases__
(<class '__main__.B'>, <class '__main__.C'>)
>>>
```

This provides a link to parent classes.
