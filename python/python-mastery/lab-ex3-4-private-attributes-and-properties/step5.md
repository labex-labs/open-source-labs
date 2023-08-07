# Reconciling Types

In the current `Stock` class, there is a `_types` class variable that gives conversions when reading from a file, but there are also properties that are enforcing types. Who is in charge of this show? Fix the property definitions so that they use the types specified in the `_types` class variable. Make sure the properties work when types are changed via subclassing. For example:

```python
>>> from decimal import Decimal
>>> class DStock(Stock):
        _types = (str, int, Decimal)

>>> s = DStock('AA', 50, Decimal('91.1'))
>>> s.price = 92.3
Traceback (most recent call last):
...
TypeError: Expected a Decimal
>>>
```

**Discussion**

The resulting `Stock` class at the end of this lab is a muddled mess of properties, type checking, constructors, and other details. Imagine how unpleasant it would be to maintain code that featured dozens or hundreds of such class definitions.

We're going to figure out how to simplify things considerably, but it's going to take some time and some more advanced techniques. Stay tuned.
