# Найти наилучшие результаты классификатора

Для каждого количества компонентов мы найдем наилучшие результаты классификатора.

```python
results = pd.DataFrame(search.cv_results_)
components_col = "param_pca__n_components"
best_clfs = results.groupby(components_col).apply(
    lambda g: g.nlargest(1, "mean_test_score")
)
```
