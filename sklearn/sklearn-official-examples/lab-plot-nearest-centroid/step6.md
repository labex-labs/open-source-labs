# Visualize the Decision Boundaries

We visualize the decision boundaries for the classifier using the DecisionBoundaryDisplay function from Scikit-learn.

```python
_, ax = plt.subplots()
DecisionBoundaryDisplay.from_estimator(
    clf, X, cmap=cmap_light, ax=ax, response_method="predict"
)
```
