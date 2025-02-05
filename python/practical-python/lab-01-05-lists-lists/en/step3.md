# List Iteration and Search

Use `for` to iterate over the list contents.

```python
for name in names:
    # use name
    # e.g. print(name)
    ...
```

This is similar to a `foreach` statement from other programming languages.

To find the position of something quickly, use `index()`.

```python
names = ['Elwood','Jake','Curtis']
names.index('Curtis')   # 2
```

If the element is present more than once, `index()` will return the index of the first occurrence.

If the element is not found, it will raise a `ValueError` exception.
