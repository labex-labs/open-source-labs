# Tracez une flèche entre des axes différents

Traçons une flèche entre le même point dans les coordonnées de données, mais dans des axes différents.

```python
xy = (0.3, 0.2)
con = ConnectionPatch(
    xyA=xy, coordsA=ax2.transData,
    xyB=xy, coordsB=ax1.transData,
    arrowstyle="->", shrinkB=5)
fig.add_artist(con)
```
