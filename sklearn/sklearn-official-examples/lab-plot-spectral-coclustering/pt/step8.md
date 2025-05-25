# Reorganizar o conjunto de dados embaralhado

Reorganizamos o conjunto de dados embaralhado para tornar os biclusters contíguos usando a função `argsort()` do numpy.

```python
fit_data = data[np.argsort(model.row_labels_)]
fit_data = fit_data[:, np.argsort(model.column_labels_)]
```
