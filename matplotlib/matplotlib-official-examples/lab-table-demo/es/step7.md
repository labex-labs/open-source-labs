# Agregar una tabla al gráfico

Agregaremos una tabla en la parte inferior del gráfico usando la función `plt.table`. Pasaremos el texto de las celdas, las etiquetas de fila, los colores de fila y las etiquetas de columna como parámetros a la función.

```python
the_table = plt.table(cellText=cell_text,
                      rowLabels=rows,
                      rowColours=colors,
                      colLabels=columns,
                      loc='bottom')
```
