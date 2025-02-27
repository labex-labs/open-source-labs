# Definir arrays para los resultados

```python
scores = np.empty((x_values.shape[0], n_splits))
amount_labeled = np.empty((x_values.shape[0], n_splits))
amount_iterations = np.empty((x_values.shape[0], n_splits))
```

Definimos arrays para almacenar los resultados de nuestro experimento.
