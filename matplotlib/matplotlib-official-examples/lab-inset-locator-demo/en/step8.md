# Create an Inset Centered in Figure Coordinates

We can create an inset that is horizontally centered in figure coordinates and vertically bound to line up with the axes by using the `blended_transform_factory()` method to create a blended transform and using it as the `bbox_transform` parameter.

```python
# Create an inset horizontally centered in figure coordinates and vertically
# bound to line up with the axes.
from matplotlib.transforms import blended_transform_factory

transform = blended_transform_factory(fig.transFigure, ax2.transAxes)
axins4 = inset_axes(ax2, width="16%", height="34%",
                    bbox_to_anchor=(0, 0, 1, 1),
                    bbox_transform=transform, loc=8, borderpad=0)
```
