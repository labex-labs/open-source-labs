# Collections

The `collections` module has a variety of classes for more specialized data
manipulation. For example, the last example could be solved with a `Counter` like this:

```python
>>> from collections import Counter
>>> totals = Counter()
>>> for s in portfolio:
        totals[s['name']] += s['shares']

>>> totals
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
>>>
```

Counters are interesting in that they support other kinds of operations such as ranking
and mathematics. For example:

```python
>>> # Get the two most common holdings
>>> totals.most_common(2)
[('MSFT', 250), ('IBM', 150)]
>>>

>>> # Adding counters together
>>> more = Counter()
>>> more['IBM'] = 75
>>> more['AA'] = 200
>>> more['ACME'] = 30
>>> more
Counter({'AA': 200, 'IBM': 75, 'ACME': 30})
>>> totals
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
>>> totals + more
Counter({'AA': 300, 'MSFT': 250, 'IBM': 225, 'CAT': 150, 'GE': 95, 'ACME': 30})
>>>
```

The `defaultdict` object can be used to group data. For example, suppose
you want to make it easy to find all matching entries for a given name such as
IBM. Try this:

```python
>>> from collections import defaultdict
>>> byname = defaultdict(list)
>>> for s in portfolio:
        byname[s['name']].append(s)

>>> byname['IBM']
[{'name': 'IBM', 'shares': 50, 'price': 91.1}, {'name': 'IBM', 'shares': 100, 'price': 70.44}]
>>> byname['AA']
[{'name': 'AA', 'shares': 100, 'price': 32.2}]
>>>
```

The key feature that makes this work is that a defaultdict
automatically initializes elements for you--allowing an insertion of a
new element and an `append()` operation to be combined together.
