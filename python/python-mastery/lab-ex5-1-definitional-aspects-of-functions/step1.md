# Preparation

In Exercise 2.6 you wrote a `reader.py` module that had a function for reading a CSV into a list of dictionaries. For example:

```python
>>> import reader
>>> port = reader.read_csv_as_dicts('portfolio.csv', [str,int,float])
>>>
```

We later expanded to that code to work with instances in Exercise 3.3:

```python
>>> import reader
>>> from stock import Stock
>>> port = reader.read_csv_as_instances('portfolio.csv', Stock)
>>>
```

Eventually the code was refactored into a collection of classes involving inheritance in Exercise 3.7. However, the code has become rather complex and convoluted.
