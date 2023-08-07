# Exercise 6.15: Code simplification

Generators expressions are often a useful replacement for small generator functions. For example, instead of writing a function like this:

```python
def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row
```

You could write something like this:

```python
rows = (row for row in rows if row['name'] in names)
```

Modify the `ticker.py` program to use generator expressions as appropriate.
