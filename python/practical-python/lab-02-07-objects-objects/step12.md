# Exercise 2.25: Making dictionaries

Remember how the `dict()` function can easily make a dictionary if you
have a sequence of key names and values? Let’s make a dictionary from
the column headers:

```python
>>> headers
['name', 'shares', 'price']
>>> converted
['AA', 100, 32.2]
>>> dict(zip(headers, converted))
{'price': 32.2, 'name': 'AA', 'shares': 100}
>>>
```

Of course, if you’re up on your list-comprehension fu, you can do the
whole conversion in a single step using a dict-comprehension:

```python
>>> { name: func(val) for name, func, val in zip(headers, types, row) }
{'price': 32.2, 'name': 'AA', 'shares': 100}
>>>
```
