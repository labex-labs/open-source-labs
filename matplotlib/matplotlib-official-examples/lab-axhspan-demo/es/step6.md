# Agregar línea vertical

Agregar líneas verticales utilizando la función `axvline()`.

```python
# Línea vertical en x=1 que abarca el rango de y.
ax.axvline(x=1)
# Línea vertical gruesa de color azul en x=0 que abarca el cuadrante superior del rango de y.
ax.axvline(x=0, ymin=0.75, linewidth=8, color='#1f77b4')
```
