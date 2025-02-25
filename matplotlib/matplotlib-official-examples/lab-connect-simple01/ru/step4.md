# Нарисуем стрелку между разными осями

Нарисуем стрелку между одной и той же точкой в координатах данных, но в разных осях.

```python
xy = (0.3, 0.2)
con = ConnectionPatch(
    xyA=xy, coordsA=ax2.transData,
    xyB=xy, coordsB=ax1.transData,
    arrowstyle="->", shrinkB=5)
fig.add_artist(con)
```
