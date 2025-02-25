# Crear un gráfico pcolormesh con texto superpuesto con rasterización

Crearemos un gráfico pcolormesh con texto superpuesto con rasterización para ilustrar cómo la rasterización puede permitir que los gráficos vectoriales mantengan las ventajas de los gráficos vectoriales para algunos artistas, como los ejes y el texto.

```python
ax4.set_aspect(1)
m = ax4.pcolormesh(xx, yy, d, zorder=-10)
ax4.text(0.5, 0.5, "Text", alpha=0.2,
         va="center", ha="center", size=50, transform=ax4.transAxes)
ax4.set_rasterization_zorder(0)
ax4.set_title("Rasterización z$<-10$")
```
