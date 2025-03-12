# Adding and Modifying Object Attributes

In Python, objects are implemented based on dictionaries. This implementation gives Python a high degree of flexibility when dealing with object attributes. Unlike some other programming languages, Python doesn't limit the attributes of an object to only those defined in its class. This means you can add new attributes to an object at any time, even after the object has been created.

Let's explore this flexibility by adding a new attribute to one of our instances. Suppose we have an instance named `goog` of a class. We'll add a `date` attribute to it:

```python
>>> goog.date = "6/11/2007"
>>> goog.__dict__
{'name': 'GOOG', 'shares': 100, 'price': 490.1, 'date': '6/11/2007'}
```

Here, we added a new attribute `date` to the `goog` instance. Notice that this `date` attribute was not defined in the `SimpleStock` class. This new attribute exists only on the `goog` instance. To confirm this, let's check the `ibm` instance:

```python
>>> ibm.__dict__
{'name': 'IBM', 'shares': 50, 'price': 91.23}
>>> hasattr(ibm, 'date')
False
```

As we can see, the `ibm` instance does not have the `date` attribute. This shows three important characteristics of Python objects:

1. Each instance has its own unique set of attributes.
2. Attributes can be added to an object after it has been created.
3. Adding an attribute to one instance does not affect other instances.

Now, let's try a different way to add an attribute. Instead of using the dot notation, we'll directly manipulate the underlying dictionary of the object. In Python, each object has a special attribute `__dict__` which stores all its attributes as key - value pairs.

```python
>>> goog.__dict__['time'] = '9:45am'
>>> goog.time
'9:45am'
>>> goog.__dict__
{'name': 'GOOG', 'shares': 100, 'price': 490.1, 'date': '6/11/2007', 'time': '9:45am'}
```

By directly modifying the `__dict__` dictionary, we added a new attribute `time` to the `goog` instance. When we access `goog.time`, Python looks for the 'time' key in the `__dict__` dictionary and returns its corresponding value.

These examples illustrate that Python objects are essentially dictionaries with some extra features. The flexibility of Python objects allows for dynamic modification, which is very powerful and convenient in programming.
