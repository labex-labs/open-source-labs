# Use cases

List comprehensions are hugely useful. For example, you can collect values of a specific dictionary fields:

```python
stocknames = [s['name'] for s in stocks]
```

You can perform database-like queries on sequences.

```python
a = [s for s in stocks if s['price'] > 100 and s['shares'] > 50 ]
```

You can also combine a list comprehension with a sequence reduction:

```python
cost = sum([s['shares']*s['price'] for s in stocks])
```
