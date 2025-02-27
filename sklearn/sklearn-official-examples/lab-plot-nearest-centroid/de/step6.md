# Visualisiere die Entscheidungsgrenzen

Wir visualisieren die Entscheidungsgrenzen für den Klassifizierer mit der DecisionBoundaryDisplay-Funktion aus Scikit-learn.

```python
_, ax = plt.subplots()
DecisionBoundaryDisplay.from_estimator(
    clf, X, cmap=cmap_light, ax=ax, response_method="predict"
)
```
