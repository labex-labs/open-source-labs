# Create a Figure with Subfigures

To create a figure with subfigures, you first need to create a figure object using `plt.figure()`. Then, you can create subfigures using `fig.subfigures()`.

```python
fig = plt.figure()
subfigs = fig.subfigures(2, 1)
```

This will create a figure with two subfigures, one above the other.
