# Creating the Plot

In this step, we will create the masked contour plot using the `contourf()` function. We pass in the `x`, `y`, and `z` arrays to this function, along with the `corner_mask` argument set to `True` or `False` depending on the type of plot we want to create.

```python
corner_masks = [False, True]
fig, axs = plt.subplots(ncols=2)
for ax, corner_mask in zip(axs, corner_masks):
    cs = ax.contourf(x, y, z, corner_mask=corner_mask)
    ax.contour(cs, colors='k')
    ax.set_title(f'{corner_mask=}')

    # Plot grid.
    ax.grid(c='k', ls='-', alpha=0.3)

    # Indicate masked points with red circles.
    ax.plot(np.ma.array(x, mask=~mask), y, 'ro')

plt.show()
```
