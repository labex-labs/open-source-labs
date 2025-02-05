# Create an Inset with a 2-Tuple Bounding Box

We can create an inset with a 2-tuple bounding box by specifying the width and height in inches and using the `bbox_to_anchor` parameter to specify the lower left corner of the inset.

```python
# Create an inset with a 2-tuple bounding box. Note that this creates a
# bbox without extent. This hence only makes sense when specifying
# width and height in absolute units (inches).
axins2 = inset_axes(ax, width=0.5, height=0.4,
                    bbox_to_anchor=(0.33, 0.25),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
```
