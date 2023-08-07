# Part 1 : Numbers

Numerical calculations work about like you would expect in Python.
For example:

```python
>>> 3 + 4*5
23
>>> 23.45 / 1e-02
2345.0
>>>
```

Be aware that integer division is different in Python 2 and Python 3.

```python
>>> 7 / 4      # In python 2, this truncates to 1
1.75
>>> 7 // 4     # Truncating division
1
>>>
```

If you want Python 3 behavior in Python 2, do this:

```python
>>> from __future__ import division
>>> 7 / 4
1.75
>>> 7 // 4      # Truncating division
1
>>>
```

Numbers have a small set of methods, many of which are actually quite
recent and overlooked by even experienced Python programmers. Try some of them.

```python
>>> x = 1172.5
>>> x.as_integer_ratio()
(2345, 2)
>>> x.is_integer()
False
>>> y = 12345
>>> y.numerator
12345
>>> y.denominator
1
>>> y.bit_length()
14
>>>
```
