# Draw an arrow between different axes

Let's draw an arrow between the same point in data coordinates, but in different axes.

```python
xy = (0.3, 0.2)
con = ConnectionPatch(
    xyA=xy, coordsA=ax2.transData,
    xyB=xy, coordsB=ax1.transData,
    arrowstyle="->", shrinkB=5)
fig.add_artist(con)
```
