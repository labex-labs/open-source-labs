# Adding axes to the figure

We will add axes to the figure using the `fig.add_axes()` method. We will also set the background color of the axes using the `rect.set_facecolor()` method.

```python
ax1 = fig.add_axes([0.1, 0.3, 0.4, 0.4])
rect = ax1.patch
rect.set_facecolor('lightslategray')
```
