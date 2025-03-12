# Understanding the Relationship Between Classes and Instances

Now let's explore how classes and instances are related in Python, and how method lookup works.

First, let's check what class our instances belong to:

```python
>>> goog.__class__
<class '__main__.SimpleStock'>
>>> ibm.__class__
<class '__main__.SimpleStock'>
```

Both instances have a reference back to the `SimpleStock` class. This reference is used when Python needs to look up methods, as we'll see next.

When you call a method on an instance, Python follows these steps:

1. It looks for the attribute in the instance's `__dict__`
2. If not found, it checks the class's `__dict__`
3. If found in the class, it returns that attribute

Let's see this in action. First, verify that the `cost` method is not in the instance dictionaries:

```python
>>> 'cost' in goog.__dict__
False
>>> 'cost' in ibm.__dict__
False
```

So where is the `cost` method coming from? Let's check the class:

```python
>>> SimpleStock.__dict__['cost']
<function SimpleStock.cost at 0x7f...>
```

The method is defined in the class, not in the instances. When you call `goog.cost()`, Python doesn't find `cost` in `goog.__dict__`, so it looks in `SimpleStock.__dict__` and finds it there.

You can actually call the method directly from the class dictionary, passing the instance as the first argument (which becomes `self`):

```python
>>> SimpleStock.__dict__['cost'](goog)
49010.0
>>> SimpleStock.__dict__['cost'](ibm)
4561.5
```

This is essentially what Python does behind the scenes when you call `goog.cost()`.

Now, let's add a class attribute. Class attributes are shared by all instances:

```python
>>> SimpleStock.exchange = 'NASDAQ'
>>> goog.exchange
'NASDAQ'
>>> ibm.exchange
'NASDAQ'
```

Both instances can access the `exchange` attribute, but it's not stored in their individual dictionaries:

```python
>>> 'exchange' in goog.__dict__
False
>>> 'exchange' in SimpleStock.__dict__
True
>>> SimpleStock.__dict__['exchange']
'NASDAQ'
```

This demonstrates that:

1. Class attributes are shared by all instances
2. Python checks the instance dictionary first, then the class dictionary
3. Classes act as a repository for shared data and behavior (methods)

If we modify an instance attribute with the same name, it shadows the class attribute:

```python
>>> ibm.exchange = 'NYSE'
>>> ibm.exchange
'NYSE'
>>> goog.exchange  # Still using the class attribute
'NASDAQ'
>>> ibm.__dict__['exchange']
'NYSE'
```

Now `ibm` has its own `exchange` attribute that shadows the class attribute, while `goog` still uses the class attribute.
