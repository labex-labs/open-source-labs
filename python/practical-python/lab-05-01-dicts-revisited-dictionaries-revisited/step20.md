# Exercise 5.3: The role of classes

The definitions that make up a class definition are shared by all
instances of that class. Notice, that all instances have a link back
to their associated class:

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

Notice that the name 'cost' is not defined in either `goog.__dict__`
or `ibm.__dict__`. Instead, it is being supplied by the class
dictionary. Try this:

```python
>>> Stock.__dict__['cost']
... look at output ...
>>>
```

Try calling the `cost()` method directly through the dictionary:

```python
>>> Stock.__dict__['cost'](goog)
49010.0
>>> Stock.__dict__['cost'](ibm)
4561.5
>>>
```

Notice how you are calling the function defined in the class
definition and how the `self` argument gets the instance.

Try adding a new attribute to the `Stock` class:

```python
>>> Stock.foo = 42
>>>
```

Notice how this new attribute now shows up on all of the instances:

```python
>>> goog.foo
42
>>> ibm.foo
42
>>>
```

However, notice that it is not part of the instance dictionary:

```python
>>> goog.__dict__
... look at output and notice there is no 'foo' attribute ...
>>>
```

The reason you can access the `foo` attribute on instances is that
Python always checks the class dictionary if it can't find something
on the instance itself.

Note: This part of the exercise illustrates something known as a class
variable. Suppose, for instance, you have a class like this:

```python
class Foo(object):
     a = 13                  # Class variable
     def __init__(self,b):
         self.b = b          # Instance variable
```

In this class, the variable `a`, assigned in the body of the
class itself, is a "class variable." It is shared by all of the
instances that get created. For example:

```python
>>> f = Foo(10)
>>> g = Foo(20)
>>> f.a          # Inspect the class variable (same for both instances)
13
>>> g.a
13
>>> f.b          # Inspect the instance variable (differs)
10
>>> g.b
20
>>> Foo.a = 42   # Change the value of the class variable
>>> f.a
42
>>> g.a
42
>>>
```
