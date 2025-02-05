# 用于超参数优化的网格搜索

我们将使用网格搜索来探索超参数空间，并为我们的支持向量机模型找到最佳超参数。

```python
# specify parameters to search over
param_grid = {
    "average": [True, False],
    "l1_ratio": np.linspace(0, 1, num=10),
    "alpha": np.power(10, np.arange(-2, 1, dtype=float)),
}

# run grid search
grid_search = GridSearchCV(clf, param_grid=param_grid)

start = time()
grid_search.fit(X, y)

print(
    "GridSearchCV took %.2f seconds for %d candidate parameter settings."
    % (time() - start, len(grid_search.cv_results_["params"]))
)

# print results
report(grid_search.cv_results_)
```
