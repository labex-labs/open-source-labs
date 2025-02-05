# 使用交叉验证执行随机搜索

随机搜索会从参数网格中随机抽取一个子集，并使用交叉验证来评估每个组合的性能。当参数空间很大且进行详尽搜索不可行时，它很有用。

```python
# 创建RandomizedSearchCV的实例
random_search = RandomizedSearchCV(svc, param_grid, cv=5, n_iter=10, random_state=0)

# 拟合数据以执行随机搜索
random_search.fit(X, y)

# 打印最佳超参数组合
print('最佳超参数:', random_search.best_params_)
```
