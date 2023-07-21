# Exercise 7.5: Sorting on a field

Try the following statements which sort the portfolio data
alphabetically by stock name.

```python
>>> def stock_name(s):
       return s.name

>>> portfolio.sort(key=stock_name)
>>> for s in portfolio:
           print(s)

... inspect the result ...
>>>
```

In this part, the `stock_name()` function extracts the name of a stock from
a single entry in the `portfolio` list. `sort()` uses the result of
this function to do the comparison.
