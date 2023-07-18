# Create Inset Axes

Next, we will create inset axes in each of the subplots. We will use the `inset_axes()` method to create the inset axes. We will create four insets with different sizes and locations.

```python
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Create inset of width 1.3 inches and height 0.9 inches
# at the default upper right location
axins = inset_axes(ax, width=1.3, height=0.9)

# Create inset of width 30% and height 40% of the parent axes' bounding box
# at the lower left corner (loc=3)
axins2 = inset_axes(ax, width="30%", height="40%", loc=3)

# Create inset of mixed specifications in the second subplot;
# width is 30% of parent axes' bounding box and
# height is 1 inch at the upper left corner (loc=2)
axins3 = inset_axes(ax2, width="30%", height=1., loc=2)

# Create an inset in the lower right corner (loc=4) with borderpad=1, i.e.
# 10 points padding (as 10pt is the default fontsize) to the parent axes
axins4 = inset_axes(ax2, width="20%", height="20%", loc=4, borderpad=1)
```
