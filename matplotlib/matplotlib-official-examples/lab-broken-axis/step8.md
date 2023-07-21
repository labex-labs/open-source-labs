# Create the Cut-Out Slanted Lines

Finally, we will create the cut-out slanted lines. We will create line objects in axes coordinates and use `ax1.transAxes` and `ax2.transAxes` to transform them to the coordinates of each subplot. We will use `ax1.plot` and `ax2.plot` to plot the lines. We will also use `marker` to specify the marker style, `markersize` to set the size of the markers, `linestyle` to set the style of the line, `color` to set the color of the line, `mec` to set the color of the marker edge, and `mew` to set the width of the marker edge.

```python
d = .5
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle="none", color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)
```
