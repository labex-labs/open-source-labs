# zip() function

The `zip` function takes multiple sequences and makes an iterator that combines them.

```python
columns = ['name', 'shares', 'price']
values = ['GOOG', 100, 490.1 ]
pairs = zip(columns, values)
# ('name','GOOG'), ('shares',100), ('price',490.1)
```

To get the result you must iterate. You can use multiple variables to unpack the tuples as shown earlier.

```python
for column, value in pairs:
    ...
```

A common use of `zip` is to create key/value pairs for constructing dictionaries.

```python
d = dict(zip(columns, values))
```
