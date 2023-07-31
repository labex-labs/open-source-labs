# Setting Properties

The pyplot interface allows us to set and get object properties for visualizing data. We can use the `setp` method to set the properties of an object. For example, to set the linestyle of a line to dashed, we use the following code:

```python
line, = plt.plot([1, 2, 3])
plt.setp(line, linestyle='--')
```

If we want to know the valid types of arguments, we can provide the name of the property we want to set without a value:

```python
plt.setp(line, 'linestyle')
```

This will return the following output:

```
linestyle: {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}
```

If we want to see all the properties that can be set, and their possible values, we can use the following code:

```python
plt.setp(line)
```

This will return a long list of properties and their possible values.
