# Crear un gráfico pcolormesh sin rasterización

Crearemos un gráfico pcolormesh sin rasterización para ilustrar la diferencia entre rasterización y no rasterización.

```python
ax1.set_aspect(1)
ax1.pcolormesh(xx, yy, d)
ax1.set_title("No Rasterización")
```
