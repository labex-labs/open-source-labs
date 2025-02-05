# Customize Axis Tick and Grid Properties

We can customize the axis tick and grid properties using the `grid()` and `tick_params()` functions. In this example, we will change the color and size of the tick labels and the width and style of the grid lines.

```python
ax.grid(True, linestyle='-.', linewidth=0.5, color='gray')
ax.tick_params(axis='both', which='both', labelsize=8, width=1, color='red')
```
