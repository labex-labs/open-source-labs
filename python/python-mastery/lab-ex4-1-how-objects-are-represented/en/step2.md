# Exploring the Internal Dictionary of Objects

Python objects store their attributes in a dictionary that can be accessed through the `__dict__` attribute. Let's examine this internal structure for our `SimpleStock` instances.

In the Python interactive shell, type the following commands to inspect the `__dict__` attribute of our instances:

```python
>>> goog.__dict__
{'name': 'GOOG', 'shares': 100, 'price': 490.1}
>>> ibm.__dict__
{'name': 'IBM', 'shares': 50, 'price': 91.23}
```

The output shows that each instance has its own internal dictionary containing all the instance attributes. This is how Python implements object attributes behind the scenes. Every object has a private dictionary that holds all of its attributes.

Note that the `__dict__` attribute reveals the internal implementation of our objects:

1. The keys in the dictionary correspond to the attribute names
2. The values in the dictionary are the attribute values
3. Each instance has its own separate `__dict__`

This dictionary-based approach allows Python to be very flexible with objects, as we will see in the next step.
