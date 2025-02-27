# Определение массивов для результатов

```python
scores = np.empty((x_values.shape[0], n_splits))
amount_labeled = np.empty((x_values.shape[0], n_splits))
amount_iterations = np.empty((x_values.shape[0], n_splits))
```

Мы определяем массивы для хранения результатов нашего эксперимента.
