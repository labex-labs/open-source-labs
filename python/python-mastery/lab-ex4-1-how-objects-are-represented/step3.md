# Modification of Instance Data

Try setting a new attribute on one of the above instances:

```python
>>> goog.date = "6/11/2007"
>>> goog.__dict__
... look at output ...
>>> ibm.__dict__
... look at output ...
>>>
```

In the above output, you'll notice that the `goog` instance has
a attribute `date` whereas the `ibm` instance does not.
It is important to note that Python really doesn't place any
restrictions on attributes. For example, the attributes of an
instance are not limited to those set up in the `__init__()`
method.

Instead of setting an attribute, try placing a new value directly into
the `__dict__` object:

```python
>>> goog.__dict__['time'] = '9:45am'
>>> goog.time
'9:45am'
>>>
```

Here, you really notice the fact that an instance is a layer on top of a dictionary.
