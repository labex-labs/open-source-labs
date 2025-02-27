# Réordonner l'ensemble de données mélangé

Nous réordonnons l'ensemble de données mélangé pour rendre les biclusters contigus à l'aide de la fonction `argsort()` de numpy.

```python
fit_data = data[np.argsort(model.row_labels_)]
fit_data = fit_data[:, np.argsort(model.column_labels_)]
```
