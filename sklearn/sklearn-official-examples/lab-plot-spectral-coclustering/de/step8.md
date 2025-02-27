# Neuordnung des gemischten Datensatzes

Wir ordnen den gemischten Datensatz neu an, um die Bicluster zusammenhängend zu machen, mit der Funktion `argsort()` aus numpy.

```python
fit_data = data[np.argsort(model.row_labels_)]
fit_data = fit_data[:, np.argsort(model.column_labels_)]
```
