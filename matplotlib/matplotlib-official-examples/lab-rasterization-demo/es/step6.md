# Crear un gráfico pcolormesh con texto superpuesto sin rasterización

Crearemos un gráfico pcolormesh con texto superpuesto sin rasterización para ilustrar cómo los gráficos vectoriales pueden mantener las ventajas de los gráficos vectoriales para algunos artistas, como los ejes y el texto.

```python
ax3.set_aspect(1)
ax3.pcolormesh(xx, yy, d)
ax3.text(0.5, 0.5, "Text", alpha=0.2,
         va="center", ha="center", size=50, transform=ax3.transAxes)
ax3.set_title("No Rasterización")
```
