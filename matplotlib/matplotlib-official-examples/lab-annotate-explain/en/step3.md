# Add an ellipse to the plot

In this step, we will add an ellipse to the plot. We will use the `Ellipse` function to create the ellipse, and we will customize the ellipse properties such as the position, width, height, and angle.

```python
ax = axs.flat[1]
ax.plot([x1, x2], [y1, y2], ".")
el = mpatches.Ellipse((x1, y1), 0.3, 0.4, angle=30, alpha=0.2)
ax.add_artist(el)
```
