# 最適な分類器の結果を見つける

主成分の数ごとに、最適な分類器の結果を見つけます。

```python
results = pd.DataFrame(search.cv_results_)
components_col = "param_pca__n_components"
best_clfs = results.groupby(components_col).apply(
    lambda g: g.nlargest(1, "mean_test_score")
)
```
