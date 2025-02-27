# Загрузка данных

```python
X, y = datasets.load_breast_cancer(return_X_y=True)
X, y = shuffle(X, y, random_state=42)
y_true = y.copy()
y[50:] = -1
total_samples = y.shape[0]
```

Загружается и перемешивается датасет `breast_cancer`. Затем истинные метки копируются в `y_true`, а из `y` удаляются все метки, кроме первых 50 образцов. Это будет использоваться для имитации сценария полунагруженного обучения.
