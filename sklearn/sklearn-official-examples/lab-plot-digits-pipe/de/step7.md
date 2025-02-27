# Finden der besten Klassifizierer-Ergebnisse

Für jede Anzahl von Komponenten werden wir die besten Klassifizierer-Ergebnisse finden.

```python
results = pd.DataFrame(search.cv_results_)
components_col = "param_pca__n_components"
best_clfs = results.groupby(components_col).apply(
    lambda g: g.nlargest(1, "mean_test_score")
)
```
