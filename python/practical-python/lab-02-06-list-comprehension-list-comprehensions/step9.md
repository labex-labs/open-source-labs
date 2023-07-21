# Exercise 2.22: Data Extraction

Show how you could build a list of tuples `(name, shares)` where `name` and `shares` are taken from `portfolio`.

```python
>>> name_shares =[ (s['name'], s['shares']) for s in portfolio ]
>>> name_shares
[('AA', 100), ('IBM', 50), ('CAT', 150), ('MSFT', 200), ('GE', 95), ('MSFT', 50), ('IBM', 100)]
>>>
```

If you change the square brackets (`[`,`]`) to curly braces (`{`, `}`), you get something known as a set comprehension.
This gives you unique or distinct values.

For example, this determines the set of unique stock names that appear in `portfolio`:

```python
>>> names = { s['name'] for s in portfolio }
>>> names
{ 'AA', 'GE', 'IBM', 'MSFT', 'CAT' }
>>>
```

If you specify `key:value` pairs, you can build a dictionary.
For example, make a dictionary that maps the name of a stock to the total number of shares held.

```python
>>> holdings = { name: 0 for name in names }
>>> holdings
{'AA': 0, 'GE': 0, 'IBM': 0, 'MSFT': 0, 'CAT': 0}
>>>
```

This latter feature is known as a **dictionary comprehension**. Let’s tabulate:

```python
>>> for s in portfolio:
        holdings[s['name']] += s['shares']

>>> holdings
{ 'AA': 100, 'GE': 95, 'IBM': 150, 'MSFT':250, 'CAT': 150 }
>>>
```

Try this example that filters the `prices` dictionary down to only
those names that appear in the portfolio:

```python
>>> portfolio_prices = { name: prices[name] for name in names }
>>> portfolio_prices
{'AA': 9.22, 'GE': 13.48, 'IBM': 106.28, 'MSFT': 20.89, 'CAT': 35.46}
>>>
```
