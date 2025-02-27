# 交差検証を用いたグリッドサーチを実行する

グリッドサーチは、指定されたパラメータグリッド内のすべてのハイパーパラメータの可能な組み合わせを網羅的に検索します。それは交差検証を使用して各組み合わせの性能を評価します。

```python
# Create an instance of GridSearchCV
grid_search = GridSearchCV(svc, param_grid, cv=5)

# Fit the data to perform grid search
grid_search.fit(X, y)

# Print the best combination of hyperparameters
print('Best hyperparameters:', grid_search.best_params_)
```
