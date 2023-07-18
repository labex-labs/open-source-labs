# Set the Limits and Display the Grid

In this step, we will set the limits for the axes and display the grid. We will use `set_aspect()` to set the aspect ratio of the axes and `grid()` to display the grid.

```python
# Set the limits and display the grid
ax1.set_aspect(1.)
ax1.set_xlim(-5, 12)
ax1.set_ylim(-5, 10)
ax1.grid(True)
```
