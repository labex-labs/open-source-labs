# Нарисуем линию между различными точками

Наконец, нарисуем линию между различными точками, определенными в разных системах координат.

```python
con = ConnectionPatch(
    # в координатах осей
    xyA=(0.6, 1.0), coordsA=ax2.transAxes,
    # x в координатах осей, y в координатах данных
    xyB=(0.0, 0.2), coordsB=ax2.get_yaxis_transform(),
    arrowstyle="-")
ax2.add_artist(con)
```
