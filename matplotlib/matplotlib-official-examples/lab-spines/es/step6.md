# Personalizar las espinas con límites limitados al rango de datos

En el tercer subgráfico, mostraremos las espinas con límites limitados al rango de datos. Podemos limitar la extensión de cada espina al rango de datos utilizando el método `set_bounds`.

```python
ax2.plot(x, y)
ax2.set_title('Spines with Bounds Limited to Data Range')

# Only draw spines for the data range, not in the margins
ax2.spines.bottom.set_bounds(x.min(), x.max())
ax2.spines.left.set_bounds(y.min(), y.max())
# Hide the right and top spines
ax2.spines.right.set_visible(False)
ax2.spines.top.set_visible(False)
```
