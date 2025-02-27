# Визуализируем границы решения

Мы визуализируем границы решения для классификатора с использованием функции DecisionBoundaryDisplay из Scikit-learn.

```python
_, ax = plt.subplots()
DecisionBoundaryDisplay.from_estimator(
    clf, X, cmap=cmap_light, ax=ax, response_method="predict"
)
```
