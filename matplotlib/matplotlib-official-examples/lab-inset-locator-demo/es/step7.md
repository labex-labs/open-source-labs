# Crear un inset con un cuadro delimitador de 2-tupla

Podemos crear un inset con un cuadro delimitador de 2-tupla especificando el ancho y la altura en pulgadas y usando el parámetro `bbox_to_anchor` para especificar la esquina inferior izquierda del inset.

```python
# Crea un inset con un cuadro delimitador de 2-tupla. Tenga en cuenta que esto crea un
# bbox sin extensión. Por lo tanto, solo tiene sentido cuando se especifica
# el ancho y la altura en unidades absolutas (pulgadas).
axins2 = inset_axes(ax, width=0.5, height=0.4,
                    bbox_to_anchor=(0.33, 0.25),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
```
