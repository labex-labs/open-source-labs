# Lists and Math

_Caution: Lists were not designed for math operations._

```python
>>> nums = [1, 2, 3, 4, 5]
>>> nums * 2
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
>>> nums + [10, 11, 12, 13, 14]
[1, 2, 3, 4, 5, 10, 11, 12, 13, 14]
```

Specifically, lists don't represent vectors/matrices as in MATLAB, Octave, R, etc. However, there are some packages to help you with that (e.g. [numpy](https://numpy.org)).

In this exercise, we experiment with Python's list datatype. In the last section, you worked with strings containing stock symbols.

```python
>>> symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
```

Split it into a list of names using the `split()` operation of strings:

```python
>>> symlist = symbols.split(',')
```
