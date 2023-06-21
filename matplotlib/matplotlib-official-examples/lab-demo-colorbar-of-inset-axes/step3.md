# Create an Inset Axis

Create an inset axis using the `zoomed_inset_axes` function. Set the zoom level and the location of the inset axis within the main plot.

```python
axins = zoomed_inset_axes(ax, zoom=2, loc='upper left')
axins.set(xticks=[], yticks=[])
```
