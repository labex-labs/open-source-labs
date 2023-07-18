# Getting Properties

We can use the `getp` method to get the properties of an object. We can use it to query the value of a single attribute:

```python
plt.getp(line, 'linewidth')
```

This will return the value of the linewidth property of the line object.

We can also use `getp` to get all the attribute/value pairs of an object:

```python
plt.getp(line)
```

This will return a long list of all the properties and their values.
