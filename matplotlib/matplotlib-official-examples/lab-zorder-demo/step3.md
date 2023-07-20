# Setting Zorder for Ticks and Grid Lines

We can use the `set_axisbelow()` method or the `axes.axisbelow` parameter to set the `zorder` of ticks and grid lines.

```python
ax = plt.axes()
ax.plot([1, 2, 3], [2, 4, 3])
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')
```
