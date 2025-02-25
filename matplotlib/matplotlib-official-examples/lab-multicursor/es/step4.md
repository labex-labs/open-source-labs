# Agregando MultiCursor

Finalmente, agregaremos la función `MultiCursor` para mostrar un cursor en los tres gráficos al pasar el cursor sobre un punto de datos.

```python
multi = MultiCursor(None, (ax1, ax2, ax3), color='r', lw=1)
plt.show()
```
