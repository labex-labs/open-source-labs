# Create a Figure with Two Adjustable Axes

In this step, we create a figure with two adjustable axes. We use the `make_axes_locatable` method to create a divider that allows the axes to be adjusted. We add a new axis to the right of the first axis using the `append_axes` method.

```python
fig = plt.figure()
ax1 = fig.add_axes([0, 0, 1, 1])
divider = make_axes_locatable(ax1)
ax2 = divider.append_axes("right", "100%", pad=0.3, sharey=ax1)
fig.add_axes(ax2)
```
