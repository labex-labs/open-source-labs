# Descriptors in action

Earlier, you created a class `Stock` that made use of
slots, properties, and other features. All of these features
are implemented using the descriptor protocol. See it in
action by trying this simple experiment.

First, create a stock object, and try looking up a few attributes:

```python
>>> s = Stock('GOOG', 100, 490.10)
>>> s.name
'GOOG'
>>> s.shares
100
>>>
```

Now, notice that these attributes are in the class dictionary.

```python
>>> Stock.__dict__.keys()
['sell', '__module__', '__weakref__', 'price', '_price', 'shares', '_shares',
'__slots__', 'cost', '__repr__', '__doc__', '__init__']
>>>
```

Try these steps which illustrate how descriptors get and set values on an instance:

```python
>>> q = Stock.__dict__['shares']
>>> q.__get__(s)
100
>>> q.__set__(s,75)
>>> s.shares
75
>>> q.__set__(s, '75')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "stock.py", line 23, in shares
    raise TypeError('Expected an integer')
TypeError: Expected an integer
>>>
```

The execution of `__get__()` and `__set__()` occurs automatically whenever you access instances.
