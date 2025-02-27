# Reordenar el conjunto de datos mezclado

Reordenamos el conjunto de datos mezclado para que los biclusters queden contiguos utilizando la función `argsort()` de numpy.

```python
fit_data = data[np.argsort(model.row_labels_)]
fit_data = fit_data[:, np.argsort(model.column_labels_)]
```
