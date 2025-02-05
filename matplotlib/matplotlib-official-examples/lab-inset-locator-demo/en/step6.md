# Create an Inset Outside the Axes

We can create an inset outside the axes by using the `bbox_to_anchor` parameter to specify a bounding box in axes coordinates that extends outside the axes.

```python
# Create an inset outside the axes
axins = inset_axes(ax, width="100%", height="100%",
                   bbox_to_anchor=(1.05, .6, .5, .4),
                   bbox_transform=ax.transAxes, loc=2, borderpad=0)
```
