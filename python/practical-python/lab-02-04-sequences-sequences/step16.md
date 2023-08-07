# Exercise 2.17: Inverting a dictionary

A dictionary maps keys to values. For example, a dictionary of stock prices.

```python
>>> prices = {
        'GOOG' : 490.1,
        'AA' : 23.45,
        'IBM' : 91.1,
        'MSFT' : 34.23
    }
>>>
```

If you use the `items()` method, you can get `(key,value)` pairs:

```python
>>> prices.items()
dict_items([('GOOG', 490.1), ('AA', 23.45), ('IBM', 91.1), ('MSFT', 34.23)])
>>>
```

However, what if you wanted to get a list of `(value, key)` pairs instead? _Hint: use `zip()`._

```python
>>> pricelist = list(zip(prices.values(),prices.keys()))
>>> pricelist
[(490.1, 'GOOG'), (23.45, 'AA'), (91.1, 'IBM'), (34.23, 'MSFT')]
>>>
```

Why would you do this? For one, it allows you to perform certain kinds of data processing on the dictionary data.

```python
>>> min(pricelist)
(23.45, 'AA')
>>> max(pricelist)
(490.1, 'GOOG')
>>> sorted(pricelist)
[(23.45, 'AA'), (34.23, 'MSFT'), (91.1, 'IBM'), (490.1, 'GOOG')]
>>>
```

This also illustrates an important feature of tuples. When used in comparisons, tuples are compared element-by-element starting with the first item. Similar to how strings are compared character-by-character.

`zip()` is often used in situations like this where you need to pair up data from different places. For example, pairing up the column names with column values in order to make a dictionary of named values.

Note that `zip()` is not limited to pairs. For example, you can use it with any number of input lists:

```python
>>> a = [1, 2, 3, 4]
>>> b = ['w', 'x', 'y', 'z']
>>> c = [0.2, 0.4, 0.6, 0.8]
>>> list(zip(a, b, c))
[(1, 'w', 0.2), (2, 'x', 0.4), (3, 'y', 0.6), (4, 'z', 0.8))]
>>>
```

Also, be aware that `zip()` stops once the shortest input sequence is exhausted.

```python
>>> a = [1, 2, 3, 4, 5, 6]
>>> b = ['x', 'y', 'z']
>>> list(zip(a,b))
[(1, 'x'), (2, 'y'), (3, 'z')]
>>>
```
