# Combine multiple visualizations

We can add additional plot elements to our visualization. Follow these steps:

1. Add a vertical line representing the mean of the sales data.

```python
ax.axvline(group_mean, ls='--', color='r')
```

2. Annotate new companies on the plot.

```python
for group in [3, 5, 8]:
    ax.text(145000, group, "New Company", fontsize=10, verticalalignment="center")
```

3. Adjust the position of the plot title.

```python
ax.title.set(y=1.05)
```
