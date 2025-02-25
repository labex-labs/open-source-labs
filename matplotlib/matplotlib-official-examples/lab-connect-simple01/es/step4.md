# Dibujar una flecha entre diferentes ejes

Vamos a dibujar una flecha entre el mismo punto en coordenadas de datos, pero en diferentes ejes.

```python
xy = (0.3, 0.2)
con = ConnectionPatch(
    xyA=xy, coordsA=ax2.transData,
    xyB=xy, coordsB=ax1.transData,
    arrowstyle="->", shrinkB=5)
fig.add_artist(con)
```
