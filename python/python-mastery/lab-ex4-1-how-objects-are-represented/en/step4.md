# Understanding the Relationship Between Classes and Instances

Now, we're going to explore how classes and instances are related in Python, and how method lookup works. This is an important concept because it helps you understand how Python finds and uses methods and attributes when you work with objects.

First, let's check what class our instances belong to. Knowing the class of an instance is crucial as it tells us where Python will look for methods and attributes related to that instance.

```python
>>> goog.__class__
<class '__main__.SimpleStock'>
>>> ibm.__class__
<class '__main__.SimpleStock'>
```

Both instances have a reference back to the `SimpleStock` class. This reference is like a pointer that Python uses when it needs to look up methods. When you call a method on an instance, Python uses this reference to find the appropriate method definition.

When you call a method on an instance, Python follows these steps:

1. It looks for the attribute in the instance's `__dict__`. The `__dict__` of an instance is like a storage area where all the instance-specific attributes are kept.
2. If not found, it checks the class's `__dict__`. The class's `__dict__` stores all the attributes and methods that are common to all instances of that class.
3. If found in the class, it returns that attribute.

Let's see this in action. First, verify that the `cost` method is not in the instance dictionaries. This step helps us understand that the `cost` method is not specific to each instance but is defined at the class level.

```python
>>> 'cost' in goog.__dict__
False
>>> 'cost' in ibm.__dict__
False
```

So where is the `cost` method coming from? Let's check the class. By looking at the class's `__dict__`, we can find out where the `cost` method is defined.

```python
>>> SimpleStock.__dict__['cost']
<function SimpleStock.cost at 0x7f...>
```

The method is defined in the class, not in the instances. When you call `goog.cost()`, Python doesn't find `cost` in `goog.__dict__`, so it looks in `SimpleStock.__dict__` and finds it there.

You can actually call the method directly from the class dictionary, passing the instance as the first argument (which becomes `self`). This shows how Python internally calls methods when you use the normal instance.method() syntax.

```python
>>> SimpleStock.__dict__['cost'](goog)
49010.0
>>> SimpleStock.__dict__['cost'](ibm)
4561.5
```

This is essentially what Python does behind the scenes when you call `goog.cost()`.

Now, let's add a class attribute. Class attributes are shared by all instances. This means that all instances of the class can access this attribute, and it's stored only once at the class level.

```python
>>> SimpleStock.exchange = 'NASDAQ'
>>> goog.exchange
'NASDAQ'
>>> ibm.exchange
'NASDAQ'
```

Both instances can access the `exchange` attribute, but it's not stored in their individual dictionaries. Let's verify this by checking the instance and class dictionaries.

```python
>>> 'exchange' in goog.__dict__
False
>>> 'exchange' in SimpleStock.__dict__
True
>>> SimpleStock.__dict__['exchange']
'NASDAQ'
```

This demonstrates that:

1. Class attributes are shared by all instances. All instances can access the same class attribute without having their own copy.
2. Python checks the instance dictionary first, then the class dictionary. This is the order in which Python looks for attributes when you try to access them on an instance.
3. Classes act as a repository for shared data and behavior (methods). The class stores all the common attributes and methods that can be used by all its instances.

If we modify an instance attribute with the same name, it shadows the class attribute. This means that when you access the attribute on that instance, Python will use the instance-specific value instead of the class-level value.

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
