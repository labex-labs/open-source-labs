# Control Inset Position and Size

We can use the `bbox_to_anchor` and `bbox_transform` parameters to control the position and size of the inset. These parameters allow for fine-grained control over the inset position and size or even to position the inset at completely arbitrary positions.

```python
# We use the axes transform as bbox_transform. Therefore, the bounding box
# needs to be specified in axes coordinates ((0, 0) is the lower left corner
# of the axes, (1, 1) is the upper right corner).
# The bounding box (.2, .4, .6, .5) starts at (.2, .4) and ranges to (.8, .9)
# in those coordinates.
# Inside this bounding box an inset of half the bounding box' width and
# three quarters of the bounding box' height is created. The lower left corner
# of the inset is aligned to the lower left corner of the bounding box (loc=3).
# The inset is then offset by the default 0.5 in units of the font size.
axins = inset_axes(ax, width="50%", height="75%",
                   bbox_to_anchor=(.2, .4, .6, .5),
                   bbox_transform=ax.transAxes, loc=3)
```
