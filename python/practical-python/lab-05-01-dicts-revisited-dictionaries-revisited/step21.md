# Exercise 5.4: Bound methods

A subtle feature of Python is that invoking a method actually involves
two steps and something known as a bound method. For example:

```python
>>> s = goog.sell
>>> s
<bound method Stock.sell of Stock('GOOG', 100, 490.1)>
>>> s(25)
>>> goog.shares
75
>>>
```

Bound methods actually contain all of the pieces needed to call a
method. For instance, they keep a record of the function implementing
the method:

```python
>>> s.__func__
<function sell at 0x10049af50>
>>>
```

This is the same value as found in the `Stock` dictionary.

```python
>>> Stock.__dict__['sell']
<function sell at 0x10049af50>
>>>
```

Bound methods also record the instance, which is the `self`
argument.

```python
>>> s.__self__
Stock('GOOG',75,490.1)
>>>
```

When you invoke the function using `()` all of the pieces come
together. For example, calling `s(25)` actually does this:

```python
>>> s.__func__(s.__self__, 25)    # Same as s(25)
>>> goog.shares
50
>>>
```
