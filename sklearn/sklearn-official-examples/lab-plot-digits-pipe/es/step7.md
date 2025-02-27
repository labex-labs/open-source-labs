# Encontrar los mejores resultados del clasificador

Para cada número de componentes, encontraremos los mejores resultados del clasificador.

```python
results = pd.DataFrame(search.cv_results_)
components_col = "param_pca__n_components"
best_clfs = results.groupby(components_col).apply(
    lambda g: g.nlargest(1, "mean_test_score")
)
```
