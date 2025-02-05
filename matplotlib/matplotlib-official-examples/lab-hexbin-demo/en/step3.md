# Create the Hexagonal Binned Plot

We will create the hexagonal binned plot using `matplotlib.pyplot.hexbin()`.

```python
fig, ax = plt.subplots(figsize=(9, 4))

hb = ax.hexbin(x, y, gridsize=50, cmap='inferno')
ax.set(xlim=xlim, ylim=ylim)
ax.set_title("Hexagon binning")

cb = fig.colorbar(hb, ax=ax, label='counts')
```

Here, we set the grid size to 50 and the color map to 'inferno'. We also add a color bar to show the count of data points within each hexagon.
