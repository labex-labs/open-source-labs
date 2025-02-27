# Graficando los resultados

Ahora, reordenamos los datos según las etiquetas de fila y columna asignadas por el modelo `SpectralBiclustering` en orden ascendente y graficamos de nuevo. Las `row_labels_` van desde 0 hasta 3, mientras que las `column_labels_` van desde 0 hasta 2, lo que representa un total de 4 clusters por fila y 3 clusters por columna.

```python
# Reordering first the rows and then the columns.
reordered_rows = data[np.argsort(model.row_labels_)]
reordered_data = reordered_rows[:, np.argsort(model.column_labels_)]

plt.matshow(reordered_data, cmap=plt.cm.Blues)
plt.title("After biclustering; rearranged to show biclusters")
_ = plt.show()
```

Como última etapa, queremos demostrar las relaciones entre las etiquetas de fila y columna asignadas por el modelo. Por lo tanto, creamos una cuadrícula con `numpy.outer`, que toma las `row_labels_` y `column_labels_` ordenadas y les suma 1 a cada una para asegurar que las etiquetas empiecen desde 1 en lugar de 0 para una mejor visualización.

```python
plt.matshow(
    np.outer(np.sort(model.row_labels_) + 1, np.sort(model.column_labels_) + 1),
    cmap=plt.cm.Blues,
)
plt.title("Checkerboard structure of rearranged data")
plt.show()
```
