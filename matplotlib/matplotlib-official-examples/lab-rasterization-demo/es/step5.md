# Crear un gráfico pcolormesh con rasterización

Crearemos un gráfico pcolormesh con rasterización para ilustrar cómo la rasterización puede acelerar la representación y generar archivos más pequeños.

```python
ax2.set_aspect(1)
ax2.set_title("Rasterización")
ax2.pcolormesh(xx, yy, d, rasterized=True)
```
