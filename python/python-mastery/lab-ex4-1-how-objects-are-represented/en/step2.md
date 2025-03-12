# Exploring the Internal Dictionary of Objects

In Python, objects are a fundamental concept. An object can be thought of as a container that holds data and has certain behaviors. One of the interesting aspects of Python objects is how they store their attributes. Attributes are like variables that belong to an object. Python stores these attributes in a special dictionary, which can be accessed through the `__dict__` attribute. This dictionary is an internal part of the object, and it's where Python keeps track of all the data associated with that object.

Let's take a closer look at this internal structure using our `SimpleStock` instances. In Python, an instance is an individual object created from a class. For example, if `SimpleStock` is a class, `goog` and `ibm` are instances of that class.

To see the internal dictionary of these instances, we can use the Python interactive shell. The Python interactive shell is a great tool for quickly testing code and seeing the results. In the Python interactive shell, type the following commands to inspect the `__dict__` attribute of our instances:

```python
>>> goog.__dict__
{'name': 'GOOG', 'shares': 100, 'price': 490.1}
>>> ibm.__dict__
{'name': 'IBM', 'shares': 50, 'price': 91.23}
```

When you run these commands, the output shows that each instance has its own internal dictionary. This dictionary contains all the instance attributes. For example, in the `goog` instance, the attributes `name`, `shares`, and `price` are stored in the dictionary with their corresponding values. This is how Python implements object attributes behind the scenes. Every object has a private dictionary that holds all of its attributes.

It's important to understand what the `__dict__` attribute reveals about the internal implementation of our objects:

1. The keys in the dictionary correspond to the attribute names. For example, in the `goog` instance, the key `'name'` corresponds to the attribute `name` of the object.
2. The values in the dictionary are the attribute values. So, the value `'GOOG'` is the value of the `name` attribute for the `goog` instance.
3. Each instance has its own separate `__dict__`. This means that the attributes of one instance are independent of the attributes of another instance. For example, the `shares` attribute of the `goog` instance can be different from the `shares` attribute of the `ibm` instance.

This dictionary-based approach allows Python to be very flexible with objects. As we will see in the next step, we can use this flexibility to modify and access object attributes in various ways.
