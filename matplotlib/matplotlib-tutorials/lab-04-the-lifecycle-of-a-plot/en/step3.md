# Create the plot

We will use the barplot visualization to represent the sales data. Follow these steps:

1. Create a figure and an axis object using `plt.subplots()`.

```python
fig, ax = plt.subplots()
```

2. Plot the data using the `barh()` method of the axis object.

```python
ax.barh(group_names, group_data)
```
