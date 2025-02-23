# Graficar los datos

Ahora graficaremos nuestros datos en los ejes que acabamos de crear. Usaremos el método `plot()` para graficar las tres ondas senoidales con diferentes colores y anchos de línea.

```python
# Graficar datos
ax.plot(X, Y1, c='C0', lw=2.5, label="Blue signal", zorder=10)
ax.plot(X, Y2, c='C1', lw=2.5, label="Orange signal")
ax.plot(X[::3], Y3[::3], linewidth=0, markersize=9,
        marker='s', markerfacecolor='none', markeredgecolor='C4',
        markeredgewidth=2.5)
```
