# Tuples

A tuple is a collection of values grouped together.

Example:

```python
s = ('GOOG', 100, 490.1)
```

Sometimes the `()` are omitted in the syntax.

```python
s = 'GOOG', 100, 490.1
```

Special cases (0-tuple, 1-tuple).

```python
t = ()            # An empty tuple
w = ('GOOG', )    # A 1-item tuple
```

Tuples are often used to represent _simple_ records or structures. Typically, it is a single _object_ of multiple parts. A good analogy: _A tuple is like a single row in a database table._

Tuple contents are ordered (like an array).

```python
s = ('GOOG', 100, 490.1)
name = s[0]                 # 'GOOG'
shares = s[1]               # 100
price = s[2]                # 490.1
```

However, the contents can't be modified.

```python
>>> s[1] = 75
TypeError: object does not support item assignment
```

You can, however, make a new tuple based on a current tuple.

```python
s = (s[0], 75, s[2])
```
