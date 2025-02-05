# Add a label to the center subplot

We add a label to the center subplot to indicate that this is a primary 3D view planes plot.

```python
label = 'mplot3d primary view planes\n' + 'ax.view_init(elev, azim, roll)'
annotate_axes(axd['L'], label, fontsize=18)
axd['L'].set_axis_off()
```
