# Instances and Classes

Instances and classes are linked together. The `__class__` attribute refers back to the class.

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.__dict__
{ 'name': 'GOOG', 'shares': 100, 'price': 490.1 }
>>> s.__class__
<class '__main__.Stock'>
>>>
```

The instance dictionary holds data unique to each instance, whereas the class dictionary holds data collectively shared by _all_ instances.
