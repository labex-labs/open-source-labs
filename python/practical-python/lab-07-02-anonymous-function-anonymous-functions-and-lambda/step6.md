# Exercise 7.6: Sorting on a field with lambda

Try sorting the portfolio according the number of shares using a `lambda` expression:

```python
>>> portfolio.sort(key=lambda s: s.shares)
>>> for s in portfolio:
        print(s)

... inspect the result ...
>>>
```

Try sorting the portfolio according to the price of each stock

```python
>>> portfolio.sort(key=lambda s: s.price)
>>> for s in portfolio:
        print(s)

... inspect the result ...
>>>
```

Note: `lambda` is a useful shortcut because it allows you to define a special processing function directly in the call to `sort()` as opposed to having to define a separate function first.
