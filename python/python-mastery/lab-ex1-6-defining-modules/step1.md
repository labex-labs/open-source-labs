# Using the import statement

In previous exercises, you wrote two programs `pcost.py` and
`stock.py`. Use the `import` statement to load these
programs and use their functionality:

```python
>>> import pcost
44671.15
>>> pcost.portfolio_cost('Data/portfolio2.dat')
19908.75
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.10)
>>> s.name
'GOOG'
>>> s.cost()
49010.0
>>>
```

If you can't get the above statements to work, you might have placed
your programs in a funny directory. Make sure you are running Python
in the same directory as your files or that the directory is included
on `sys.path`.
