# 优化超参数

在上一步中，我们对 alpha 和 gamma 使用了默认的超参数值。为了提高模型的性能，我们可以使用网格搜索来优化这些超参数。

```python
from sklearn.model_selection import GridSearchCV

# 定义参数网格
param_grid = {'alpha': [1e-3, 1e-2, 1e-1, 1, 10],
              'gamma': [1e-3, 1e-2, 1e-1, 1, 10]}

# 执行网格搜索
grid_search = GridSearchCV(krr, param_grid, cv=5)
grid_search.fit(X, y)

# 获取最佳超参数
best_alpha = grid_search.best_params_['alpha']
best_gamma = grid_search.best_params_['gamma']
best_krr = grid_search.best_estimator_

print("最佳 alpha:", best_alpha)
print("最佳 gamma:", best_gamma)
```
