# Adding and Modifying Object Attributes

Python's dictionary-based implementation of objects makes it very flexible when working with attributes. Unlike some other languages, Python does not restrict attributes to only those defined in the class.

Let's explore this flexibility by adding a new attribute to one of our instances:

```python
>>> goog.date = "6/11/2007"
>>> goog.__dict__
{'name': 'GOOG', 'shares': 100, 'price': 490.1, 'date': '6/11/2007'}
```

Notice that we were able to add a new attribute `date` that wasn't defined in the `SimpleStock` class. This attribute exists only on the `goog` instance. Let's verify it's not on the `ibm` instance:

```python
>>> ibm.__dict__
{'name': 'IBM', 'shares': 50, 'price': 91.23}
>>> hasattr(ibm, 'date')
False
```

As expected, the `ibm` instance doesn't have a `date` attribute. This demonstrates that in Python:

1. Each instance has its own separate set of attributes
2. Attributes can be added dynamically after an object is created
3. Adding an attribute to one instance doesn't affect other instances

Now, let's try a different approach by directly manipulating the underlying dictionary:

```python
>>> goog.__dict__['time'] = '9:45am'
>>> goog.time
'9:45am'
>>> goog.__dict__
{'name': 'GOOG', 'shares': 100, 'price': 490.1, 'date': '6/11/2007', 'time': '9:45am'}
```

This demonstrates that modifying the `__dict__` directly is another way to add attributes to an object. When you access `goog.time`, Python looks up the 'time' key in the `__dict__` dictionary.

These examples show that Python objects are essentially just dictionaries with some additional features. The flexible nature of Python objects allows for dynamic modification, which is both powerful and convenient.
