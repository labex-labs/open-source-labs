# Arrays für die Ergebnisse definieren

```python
scores = np.empty((x_values.shape[0], n_splits))
amount_labeled = np.empty((x_values.shape[0], n_splits))
amount_iterations = np.empty((x_values.shape[0], n_splits))
```

Wir definieren Arrays, um die Ergebnisse unseres Experiments zu speichern.
