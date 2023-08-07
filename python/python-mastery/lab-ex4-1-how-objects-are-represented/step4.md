# The role of classes

The definitions that make up a class definition are shared by all instances of that class. Notice, that all instances have a link back to their associated class:

```python
>>> goog.__class__
... look at output ...
>>> ibm.__class__
... look at output ...
>>>
```

Try calling a method on the instances:

```python
>>> goog.cost()
49010.0
>>> ibm.cost()
4561.5
>>>
```

Notice that the name 'cost' is not defined in either `goog.__dict__` or `ibm.__dict__`. Instead, it is being supplied by the class dictionary. Try this:

```python
>>> SimpleStock.__dict__['cost']
... look at output ...
>>>
```

Try calling the `cost()` method directly through the dictionary:

```python
>>> SimpleStock.__dict__['cost'](goog)
49010.00
>>> SimpleStock.__dict__['cost'](ibm)
4561.5
>>>
```

Notice how you are calling the function defined in the class definition and how the `self` argument gets the instance.

If you add a new value to the class, it becomes a class variable that's visible to all instances. Try it:

```python
>>> SimpleStock.spam = 42
>>> ibm.spam
42
>>> goog.spam
42
>>>
```

Observe that `spam` is not part of the instance dictionary.

```python
>>> ibm.__dict__
... look at the output ...
>>>
```

Instead, it's part of the class dictionary:

```python
>>> SimpleStock.__dict__['spam']
42
>>>
```

Essentially this is all a class really is--it's a collection of values shared by instances.
