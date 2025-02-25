# Crear un gráfico de barras apiladas verticales

Crearemos un gráfico de barras apiladas verticales usando la función `plt.bar` para representar las pérdidas causadas por diferentes desastres naturales a lo largo de los años. Usaremos un bucle `for` para iterar sobre cada fila de datos y trazar las barras.

```python
n_rows = len(data)

index = np.arange(len(columns)) + 0.3
bar_width = 0.4

y_offset = np.zeros(len(columns))

cell_text = []
for row in range(n_rows):
    plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
    y_offset = y_offset + data[row]
    cell_text.append(['%1.1f' % (x / 1000.0) for x in y_offset])
```
