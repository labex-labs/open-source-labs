# Draw a line between the different points

Finally, let's draw a line between the different points, defined in different coordinate systems.

```python
con = ConnectionPatch(
    # in axes coordinates
    xyA=(0.6, 1.0), coordsA=ax2.transAxes,
    # x in axes coordinates, y in data coordinates
    xyB=(0.0, 0.2), coordsB=ax2.get_yaxis_transform(),
    arrowstyle="-")
ax2.add_artist(con)
```

#
