# Make Room for Y-Label and Adjust Axes

In this step, we use the `make_axes_area_auto_adjustable` method to make room for the y-label in both axes. We also use the `use_axes` parameter to specify the axes to be adjusted and the `pad` parameter to adjust the spacing between the axes.

```python
make_axes_area_auto_adjustable(ax1, pad=0.1, use_axes=[ax1, ax2])
make_axes_area_auto_adjustable(ax2, pad=0.1, use_axes=[ax1, ax2])
```
