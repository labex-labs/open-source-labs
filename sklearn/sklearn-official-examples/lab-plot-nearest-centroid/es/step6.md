# Visualizar los límites de decisión

Visualizamos los límites de decisión del clasificador utilizando la función DecisionBoundaryDisplay de Scikit-learn.

```python
_, ax = plt.subplots()
DecisionBoundaryDisplay.from_estimator(
    clf, X, cmap=cmap_light, ax=ax, response_method="predict"
)
```
