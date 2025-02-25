# Dibujar una línea entre puntos diferentes

Finalmente, vamos a dibujar una línea entre puntos diferentes, definidos en diferentes sistemas de coordenadas.

```python
con = ConnectionPatch(
    # en coordenadas de eje
    xyA=(0.6, 1.0), coordsA=ax2.transAxes,
    # x en coordenadas de eje, y en coordenadas de datos
    xyB=(0.0, 0.2), coordsB=ax2.get_yaxis_transform(),
    arrowstyle="-")
ax2.add_artist(con)
```
