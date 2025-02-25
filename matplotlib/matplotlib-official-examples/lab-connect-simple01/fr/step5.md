# Tracez une ligne entre des points différents

Enfin, traçons une ligne entre des points différents, définis dans des systèmes de coordonnées différents.

```python
con = ConnectionPatch(
    # dans les coordonnées d'axe
    xyA=(0.6, 1.0), coordsA=ax2.transAxes,
    # x dans les coordonnées d'axe, y dans les coordonnées de données
    xyB=(0.0, 0.2), coordsB=ax2.get_yaxis_transform(),
    arrowstyle="-")
ax2.add_artist(con)
```
