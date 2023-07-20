# Generator Expressions and Reduction Functions

Generator expressions are especially useful for feeding data into
functions such as `sum()`, `min()`, `max()`,
`any()`, etc. Try some examples using the portfolio data from
earlier. Carefully observe that these examples are missing some
extra square brackets ([]) that appeared when using list comprehensions.

```python
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('Data/portfolio.csv')
>>> sum(s['shares']*s['price'] for s in portfolio)
44671.15
>>> min(s['shares'] for s in portfolio)
50
>>> any(s['name'] == 'IBM' for s in portfolio)
True
>>> all(s['name'] == 'IBM' for s in portfolio)
False
>>> sum(s['shares'] for s in portfolio if s['name'] == 'IBM')
150
>>>
```

Here is an subtle use of a generator expression in making comma
separated values:

```python
>>> s = ('GOOG',100,490.10)
>>> ','.join(s)
... observe that it fails ...
>>> ','.join(str(x) for x in s)    # This works
'GOOG,100,490.1'
>>>
```

The syntax in the above examples takes some getting used to, but the
critical point is that none of the operations ever create a fully
populated list of results. This gives you a big memory savings. However,
you do need to make sure you don't go overboard with the syntax.
