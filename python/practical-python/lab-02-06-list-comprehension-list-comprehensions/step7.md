# Exercise 2.20: Sequence Reductions

Compute the total cost of the portfolio using a single Python statement.

```python
>>> portfolio = read_portfolio('Data/portfolio.csv')
>>> cost = sum([ s['shares'] * s['price'] for s in portfolio ])
>>> cost
44671.15
>>>
```

After you have done that, show how you can compute the current value of the portfolio using a single statement.

```python
>>> value = sum([ s['shares'] * prices[s['name']] for s in portfolio ])
>>> value
28686.1
>>>
```

Both of the above operations are an example of a map-reduction. The list comprehension is mapping an operation across the list.

```python
>>> [ s['shares'] * s['price'] for s in portfolio ]
[3220.0000000000005, 4555.0, 12516.0, 10246.0, 3835.1499999999996, 3254.9999999999995, 7044.0]
>>>
```

The `sum()` function is then performing a reduction across the result:

```python
>>> sum(_)
44671.15
>>>
```

With this knowledge, you are now ready to go launch a big-data startup company.
