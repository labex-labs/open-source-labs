# Sticky Edges

Some plotting functions in Matplotlib make the axis limits "sticky" or immune to the `margins()` method. For instance, `imshow()` and `pcolor()` expect the user to want the limits to be tight around the pixels shown in the plot. If this behavior is not desired, you need to set `use_sticky_edges` to `False`. In this step, we will learn how to work around sticky edges in Matplotlib.

```python
# create a grid
y, x = np.mgrid[:5, 1:6]

# define polygon coordinates
poly_coords = [
    (0.25, 2.75), (3.25, 2.75),
    (2.25, 0.75), (0.25, 0.75)
]

# create subplots
fig, (ax1, ax2) = plt.subplots(ncols=2)

# use sticky edges for ax1 and turn off sticky edges for ax2
ax2.use_sticky_edges = False

# plot on both subplots
for ax, status in zip((ax1, ax2), ('Is', 'Is Not')):
    cells = ax.pcolor(x, y, x+y, cmap='inferno', shading='auto') # sticky
    ax.add_patch(
        Polygon(poly_coords, color='forestgreen', alpha=0.5)
    ) # not sticky
    ax.margins(x=0.1, y=0.05)
    ax.set_aspect('equal')
    ax.set_title(f'{status} Sticky')

plt.show()
```
