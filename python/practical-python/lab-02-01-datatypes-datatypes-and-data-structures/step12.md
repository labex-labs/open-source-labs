# Exercise 2.2: Dictionaries as a data structure

An alternative to a tuple is to create a dictionary instead.

```python
>>> d = {
        'name' : row[0],
        'shares' : int(row[1]),
        'price'  : float(row[2])
    }
>>> d
{'name': 'AA', 'shares': 100, 'price': 32.2 }
>>>
```

Calculate the total cost of this holding:

```python
>>> cost = d['shares'] * d['price']
>>> cost
3220.0000000000005
>>>
```

Compare this example with the same calculation involving tuples above. Change the number of shares to 75.

```python
>>> d['shares'] = 75
>>> d
{'name': 'AA', 'shares': 75, 'price': 32.2 }
>>>
```

Unlike tuples, dictionaries can be freely modified. Add some attributes:

```python
>>> d['date'] = (6, 11, 2007)
>>> d['account'] = 12345
>>> d
{'name': 'AA', 'shares': 75, 'price':32.2, 'date': (6, 11, 2007), 'account': 12345}
>>>
```
