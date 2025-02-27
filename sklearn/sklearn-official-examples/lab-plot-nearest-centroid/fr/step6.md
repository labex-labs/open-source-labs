# Visualisez les limites de décision

Nous visualisons les limites de décision du classifieur à l'aide de la fonction DecisionBoundaryDisplay de Scikit-learn.

```python
_, ax = plt.subplots()
DecisionBoundaryDisplay.from_estimator(
    clf, X, cmap=cmap_light, ax=ax, response_method="predict"
)
```
