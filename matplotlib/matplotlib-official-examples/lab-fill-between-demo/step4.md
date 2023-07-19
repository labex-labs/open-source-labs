# Selectively Marking Horizontal Regions Across the Whole Axes

The same selection mechanism can be applied to fill the full vertical height of the axes. To be independent of y-limits, we add a transform that interprets the x-values in data coordinates and the y-values in axes coordinates. The following example marks the regions in which the y-data are above a given threshold.

```python
fig, ax = plt.subplots()
x = np.arange(0, 4 * np.pi, 0.01)
y = np.sin(x)
ax.plot(x, y, color='black')

threshold = 0.75
ax.axhline(threshold, color='green', lw=2, alpha=0.7)
ax.fill_between(x, 0, 1, where=y > threshold,
                color='green', alpha=0.5, transform=ax.get_xaxis_transform())
```
