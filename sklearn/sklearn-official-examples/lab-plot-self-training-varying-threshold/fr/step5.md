# Définition d tableaux pour les résultats

```python
scores = np.empty((x_values.shape[0], n_splits))
amount_labeled = np.empty((x_values.shape[0], n_splits))
amount_iterations = np.empty((x_values.shape[0], n_splits))
```

Nous définissons des tableaux pour stocker les résultats de notre expérience.
