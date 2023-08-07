# Customize the Colors

We can customize the colors of the slices by passing a list of colors to the `colors` parameter of the `pie()` function.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=['olivedrab', 'rosybrown', 'gray', 'saddlebrown'])
```
