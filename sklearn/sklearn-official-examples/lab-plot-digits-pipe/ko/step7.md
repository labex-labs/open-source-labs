# 최적 분류기 결과 찾기

각 구성 요소 수에 대해 최적의 분류기 결과를 찾습니다.

```python
results = pd.DataFrame(search.cv_results_)
components_col = "param_pca__n_components"
best_clfs = results.groupby(components_col).apply(
    lambda g: g.nlargest(1, "mean_test_score")
)
```
