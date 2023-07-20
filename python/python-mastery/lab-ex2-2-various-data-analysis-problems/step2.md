# Comprehensions

List, set, and dictionary comprehensions can be a useful tool for manipulating
data. For example, try these operations:

```python
>>> # Find all holdings more than 100 shares
>>> [s for s in portfolio if s['shares'] > 100]
[{'name': 'CAT', 'shares': 150, 'price': 83.44},
 {'name': 'MSFT', 'shares': 200, 'price': 51.23}]

>>> # Compute total cost (shares * price)
>>> sum([s['shares']*s['price'] for s in portfolio])
44671.15
>>>

>>> # Find all unique stock names (set)
>>> { s['name'] for s in portfolio }
{'MSFT', 'IBM', 'AA', 'GE', 'CAT'}
>>>

>>> # Count the total shares of each of stock
>>> totals = { s['name']: 0 for s in portfolio }
>>> for s in portfolio:
        totals[s['name']] += s['shares']

>>> totals
{'AA': 100, 'IBM': 150, 'CAT': 150, 'MSFT': 250, 'GE': 95}
>>>
```
