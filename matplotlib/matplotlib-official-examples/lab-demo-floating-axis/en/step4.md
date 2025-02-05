# Create the Host Axes

In this step, we will create the host axes and set the grid helper. We will use `fig.add_subplot()` to create the host axes.

```python
# Create the host axes
fig = plt.figure(figsize=(5, 5))
ax1 = fig.add_subplot(axes_class=HostAxes, grid_helper=grid_helper)
```
