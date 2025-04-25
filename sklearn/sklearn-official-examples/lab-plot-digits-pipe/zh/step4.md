# 执行 GridSearchCV

我们将执行 GridSearchCV，以找到主成分分析（PCA）截断和分类器正则化的最佳组合。

```python
search = GridSearchCV(pipe, param_grid, n_jobs=2)
search.fit(X_digits, y_digits)
```
