# Visualizar as Fronteiras de Decisão

Visualizamos as fronteiras de decisão do classificador usando a função `DecisionBoundaryDisplay` do Scikit-learn.

```python
_, ax = plt.subplots()
DecisionBoundaryDisplay.from_estimator(
    clf, X, cmap=cmap_light, ax=ax, response_method="predict"
)
```
